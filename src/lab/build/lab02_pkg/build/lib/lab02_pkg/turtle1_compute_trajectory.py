import rclpy
from rclpy.node import Node
import math

from turtlesim.msg import Pose
import numpy as np
from geometry_msgs.msg import Point
from turtlesim.action import RotateAbsolute
from rclpy.action import ActionClient

from lab02_interfaces.srv import ComputeTrajectory

class ComputeTrajectoryService(Node):

    def __init__(self):
        super().__init__('compute_trajectory_node')
        self.srv = self.create_service(ComputeTrajectory, '/turtle1/compute_trajectory', self.compute_trajectory_callback)
        self.__turtle_pose_subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.turtle_pose_subscriber_callback, 10)
        self.turtle_pose = Pose()

    def turtle_pose_subscriber_callback(self, msg):
        self.turtle_pose = msg

    def compute_trajectory_callback(self, request, response):
        def get_angle_pose_point(tur_x, tur_y, tur_theta, req_x, req_y):
            vector_origo_to_request = np.array([req_x - tur_x, req_y - tur_y])
            angle = np.arctan2(vector_origo_to_request[1], vector_origo_to_request[0])
            return angle
        def get_distance_points(x1, y1, x2, y2):
            return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
        response.distance = get_distance_points(request.x, request.y, self.turtle_pose.x, self.turtle_pose.y)
        response.direction = get_angle_pose_point(self.turtle_pose.x, self.turtle_pose.y, self.turtle_pose.theta, request.x, request.y)
        self.get_logger().info("direction: " + str(response.direction) + "  distance: " + str(response.distance))

        return response


def main():
    rclpy.init()

    minimal_service = ComputeTrajectoryService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()