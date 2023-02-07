#!/usr/bin/env python

import rclpy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO

_FREQUENCY = 20

def _clip(value, minimum, maximum):
   """Ensure value is between minimum and maximum."""

   if value < minimum:
       return minimum
   elif value > maximum:
       return maximum
   return value

class Motor:
   def __init__(self, forward_pin, backward_pin):
       GPIO.setup(forward_pin, GPIO.OUT)
       GPIO.setup(backward_pin, GPIO.OUT)

       self._forward_pwm = GPIO.PWM(forward_pin, _FREQUENCY)
       self._backward_pwm = GPIO.PWM(backward_pin, _FREQUENCY)

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

class Driver:
   def __init__(self):
       self.node = rclpy.create_node('driver')

       self._last_received = self.node.get_clock().now().to_msg().clock
       self._timeout = self.node.get_parameter('timeout').value
       self._rate = self.node.get_parameter('rate').value
       self._max_speed = self.node.get_parameter('max_speed').value
       self._wheel_base = self.node.get_parameter('wheel_base').value

       # Assign pins to motors. These may be distributed
       # differently depending on how you've built your robot
       self._left_motor = Motor(10, 9)
       self._right_motor = Motor(8, 7)
       self._left_speed_percent = 0
       self._right_speed_percent = 0

       self._sub = self.node.create_subscription(Twist, 'cmd_vel', self._velocity_received_callback)

   def _velocity_received_callback(self, message):
       """Handle new velocity command message."""

       self._last_received = self.node.get_clock().now().to_msg().clock

       # Extract linear and angular velocities from the message
       linear = message.linear.x
       angular = message.angular.z

       # Calculate wheel speeds in m/s
       left_speed = linear - angular*self._wheel_base/2
       right_speed = linear + angular*self._wheel_base/2
   
   def run(self):
        """The control loop of the driver."""

        rate = rclpy.Rate(self._rate)

        while rclpy.ok():
            # If we haven't received new commands for a while, we
            # may have lost contact with the commander-- stop
            # moving
            delay = self._node.get_clock().now().to_sec() - self._last_received
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
    rclpy.spin(driver)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
