import rclpy
from rclpy import qos
from sensor_msgs.msg import Imu
from rclpy.node import Node

class ImuSubscriber(Node):
    def __init__(self):

        super().__init__('ImuSubscriber')
        self.imu_sub = self.create_subscription(Imu, 'camera/accel/sample', self.imu_callback, qos.qos_profile_sensor_data)

    def imu_callback(self, msg):
        print(msg)
        print("inside callback")

def main(args=None):
    rclpy.init(args=args)
    imu_subscriber = ImuSubscriber()
    rclpy.spin(imu_subscriber)

    imu_subscriber.destroy_node()
    rclpy.shutdown()

main()