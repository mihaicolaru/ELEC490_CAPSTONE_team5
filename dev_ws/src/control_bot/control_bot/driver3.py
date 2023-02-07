#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import RPi.GPIO as GPIO

# Set the GPIO modes
GPIO.setmode(GPIO.TEGRA_SOC)
GPIO.setwarnings(False)

MOT_1 = 'GPIO_PE6'      # 33

IN_A = 'DAP4_SCLK'      # 12
IN_B = 'GPIO_PZ0'       # 31

MOT_2 = 'LCD_BL_PW'     # 32

IN_C = 'SPI1_MOSI'      # 19
IN_D = 'CAM_AF_EN'      # 29

_FREQUENCY = 20

def _clip(value, minimum, maximum):
   """Ensure value is between minimum and maximum."""

   if value < minimum:
       return minimum
   elif value > maximum:
       return maximum
   return value

class Motor:
   def __init__(self, pin, IN_1, IN_2):
    GPIO.setup(pin, GPIO.OUT)

    GPIO.setup(IN_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN_2, GPIO.OUT, initial=GPIO.LOW)

    

   def move(self, speed_percent):
       speed = _clip(abs(speed_percent), 0, 100)

       # Positive speeds move wheels forward, negative speeds
       # move wheels backward
       if speed_percent < 0:
           self._backward_pwm.start(speed)
           self._forward_pwm.start(0)
       else:
           self._forward_pwm.start(speed)
           self._backward_pwm.start(0)

class Driver(Node):
   def __init__(self):
       super().__init__('driver')
       self._last_received = rclpy.get_time()
       self._timeout = rclpy.get_param('~timeout', 2)
       self._rate = rclpy.get_param('~rate', 10)
       self._max_speed = rclpy.get_param('~max_speed', 0.5)
       self._wheel_base = rclpy.get_param('~wheel_base', 0.091)

       # Assign pins to motors. These may be distributed
       # differently depending on how you've built your robot
       pwm1 = GPIO.PWM(MOT_1, 50)   # Initialize PWM on pwmPin 50Hz frequency
       pwm2 = GPIO.PWM(MOT_2, 50)   # Initialize PWM on pwmPin 50Hz frequency
       self._left_motor = Motor(MOT_1, IN_A, IN_B)
       self._right_motor = Motor(MOT_2, IN_C, IN_D)
       self._left_speed_percent = 0
       self._right_speed_percent = 0

       # Setup subscriber for velocity twist message
       rclpy.Subscriber(
           'cmd_vel', Twist, self._velocity_received_callback)

   def _velocity_received_callback(self, message):
       """Handle new velocity command message."""

       self._last_received = rclpy.get_time()

       # Extract linear and angular velocities from the message
       linear = message.linear.x
       angular = message.angular.z

       # Calculate wheel speeds in m/s
       left_speed = linear - angular*self._wheel_base/2
       right_speed = linear + angular*self._wheel_base/2

       # Ideally we'd now use the desired wheel speeds along
       # with data from wheel speed sensors to come up with the
       # power we need to apply to the wheels, but we don't have
       # wheel speed sensors. Instead, we'll simply convert m/s
       # into percent of maximum wheel speed, which gives us a
       # duty cycle that we can apply to each motor.
       self._left_speed_percent = (100 * left_speed/self._max_speed)
       self._right_speed_percent = (100 * right_speed/self._max_speed)

   def run(self):
       """The control loop of the driver."""

       rate = rclpy.Rate(self._rate)

       while not rclpy.is_shutdown():
           # If we haven't received new commands for a while, we
           # may have lost contact with the commander-- stop
           # moving
           delay = rclpy.get_time() - self._last_received
           if delay < self._timeout:
               self._left_motor.move(self._left_speed_percent)
               self._right_motor.move(self._right_speed_percent)
           else:
               self._left_motor.move(0)
               self._right_motor.move(0)

           rate.sleep()

def main(args=None):
   rclpy.init(args=args)

   driver = Driver()

   # Run driver. This will block
   driver.run()
   GPIO.cleanup()
   rclpy.spin(driver)
   driver.destroy_node()
   rclpy.shutdown()


if __name__ == '__main__':
   main()
