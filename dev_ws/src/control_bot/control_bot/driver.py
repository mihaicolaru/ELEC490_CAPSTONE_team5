import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
import math
import RPi.GPIO as GPIO

# motor setup
MOT_1 = 'GPIO_PE6'      # 33

IN_A = 'DAP4_SCLK'      # 12
IN_B = 'GPIO_PZ0'       # 31

MOT_2 = 'LCD_BL_PW'     # 32

IN_C = 'SPI1_MOSI'      # 19
IN_D = 'CAM_AF_EN'      # 29


def _clip(value, minimum, maximum):
    if value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    return value

# should relat to Driver in ROS code
class TwistToPWMMode(Node):
    def __init__(self):

        super().__init__('twist_to_pwm_node')

        # TODO: figure what these variables are and how they are used
        self.__max_speed = 0.5
        self.__wheel_base = 0.245
        
        self._left_speed_percent = 0
        self._right_speed_percent = 0
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)

        GPIO.output(IN_A, GPIO.LOW)
        GPIO.output(IN_B, GPIO.LOW)
        GPIO.output(IN_C, GPIO.LOW)
        GPIO.output(IN_D, GPIO.LOW)

        pwm1.start(0)                      # Start PWM with 0% duty cycle
        pwm2.start(0)                      # Start PWM with 0% duty cycle


    def cmd_vel_callback(self, msg):
        #need logic to process Twist message here
        linear = msg.linear.x
        angular = msg.angular.z
        self.get_logger().info('Received Twist message: linear_x={0}, angular_z={1}'.format(linear, angular))
        left_speed = linear - angular*self.__wheel_base/2
        right_speed = linear + angular*self.__wheel_base/2

        self._left_speed_percent = (100 * left_speed/self.__max_speed)
        self._right_speed_percent = (100 * right_speed/self.__max_speed)
        self.run()

    def run(self):
        print("writing to pwm")
        left_speed = _clip(abs(self._left_speed_percent), 0, 95)
        right_speed = _clip(abs(self._right_speed_percent), 0, 95)
        self.get_logger().info('Received left and right speed: left_speed={0}, right_speed={1}'.format(self._left_speed_percent, self._right_speed_percent))
        # if speed percent is negative, turn wheel backwards
        # else turn wheel forwards
        # write to pwm (values in self._left_speed_percent and self._right_speed_percent)

        if(self._left_speed_percent < 0):
            self.get_logger().info('turn left wheel backwards PWM = {0}'.format(math.floor(left_speed)))
            # set direction
            GPIO.output(IN_C, GPIO.HIGH)
            GPIO.output(IN_D, GPIO.LOW)
            #set speed
            pwm2.ChangeDutyCycle(left_speed)
        else:
            self.get_logger().info('turn left wheel forward PWM = {0}'.format(math.floor(left_speed)))
            # set direction
            GPIO.output(IN_C, GPIO.LOW)
            GPIO.output(IN_D, GPIO.HIGH)
            #set speed
            pwm2.ChangeDutyCycle(left_speed)

        if(self._right_speed_percent < 0):
            self.get_logger().info('turn right wheel backwards PWM = {0}'.format(math.floor(right_speed)))
            GPIO.output(IN_A, GPIO.LOW)
            GPIO.output(IN_B, GPIO.HIGH)
            pwm1.ChangeDutyCycle(right_speed)
        else:
            self.get_logger().info('turn right wheel forward PWM = {0}'.format(math.floor(right_speed)))
            GPIO.output(IN_A, GPIO.HIGH)
            GPIO.output(IN_B, GPIO.LOW)
            pwm1.ChangeDutyCycle(right_speed)
            


__FREQUENCY = 50
GPIO.setmode(GPIO.TEGRA_SOC)

GPIO.setup(MOT_1, GPIO.OUT)
GPIO.setup(MOT_2, GPIO.OUT)

GPIO.setup(IN_A, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN_B, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(IN_C, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN_D, GPIO.OUT, initial=GPIO.LOW)

pwm1 = GPIO.PWM(MOT_1, 50)   # Initialize PWM on pwmPin 50Hz frequency
pwm2 = GPIO.PWM(MOT_2, 50)   # Initialize PWM on pwmPin 50Hz frequency


def main(args=None):
    rclpy.init(args=args)
    node = TwistToPWMMode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

    GPIO.output(IN_A, GPIO.LOW)
    GPIO.output(IN_B, GPIO.LOW)
    GPIO.output(IN_C, GPIO.LOW)
    GPIO.output(IN_D, GPIO.LOW)

    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)

    pwm1.stop()     # stop PWM1
    pwm2.stop()     # stop PWM2
    GPIO.cleanup()
main()
# if __name__ == '__main__':
#     main()
