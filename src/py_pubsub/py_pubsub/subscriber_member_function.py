# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# import RPi.GPIO as GPIO
# from adafruit_servokit import ServoKit
# import time
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

    
# def testLED(whichLED):
#     print("Testing LED: #" + whichLED)

# def testLocking(whichLock):
#     print("Testing Lock: #" + whichLock)

# def testPWM():
#     print("Testing PWM")

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warnin

    def listener_callback(self, msg):
        minimal_subscriber = MinimalSubscriber()
        self.get_logger().info('I heard: "%s"' % msg.data)
        if(msg.data[0] == '1'):
            testLED(msg.data[1])
        elif(msg.data[0] == '2'):
            testLocking(msg.data[1])
        elif(msg.data == '3'):
            testPWM()
        elif(msg.data == '4'):
            minimal_subscriber.destroy_node()
            rclpy.shutdown()
        else:
            print("no new commands")


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
