from lab02_interfaces.srv import ComputeTrajectory

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose 

class ComputeTrajectoryService(Node):

    def __init__(self):
        super().__init__('compute_trajectory_node')
        self.srv = self.create_service(ComputeTrajectory, 'compute_trajectory', self.compute_trajectory_callback)
        self.__turtle_pose_subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.turtle_pose_subscriber_callback, 10)
        self.turtle_pose = Pose()

    def turtle_pose_subscriber_callback(self, msg):
        self.turtle_pose = msg


    def compute_trajectory_callback(self, request, response):
        # skriv matte her TODO
        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()