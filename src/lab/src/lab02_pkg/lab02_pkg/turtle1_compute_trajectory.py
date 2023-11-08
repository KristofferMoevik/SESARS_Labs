from lab02_interfaces.srv import ComputeTrajectory

import rclpy
from rclpy.node import Node
import math

from turtlesim.msg import Pose
import numpy as np
from geometry_msgs.msg import Point
from turtlesim.action import RotateAbsolute
from rclpy.action import ActionClient


class ComputeTrajectoryService(Node):

    def __init__(self):
        super().__init__('compute_trajectory_node')
        self.srv = self.create_service(ComputeTrajectory, 'compute_trajectory', self.compute_trajectory_callback)
        self.__turtle_pose_subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.turtle_pose_subscriber_callback, 10)
        self.__rotate_absolute_action_client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')
        self.turtle_pose = Pose()

    def turtle_pose_subscriber_callback(self, msg):
        #self.get_logger().info("turtle pose: x=" + str(msg.x) + " y=" + str(msg.y) + " theta=" + str(msg.theta))
        self.turtle_pose = msg


    def compute_trajectory_callback(self, request, response):
        response.distance = self.get_distance_points(request.x, request.y, self.turtle_pose.x, self.turtle_pose.y)
        response.direction = self.get_angle_pose_point(self.turtle_pose.x, self.turtle_pose.y, self.turtle_pose.theta, request.x, request.y)
        return response

    def get_angle_pose_point(self, tur_x, tur_y, tur_theta, req_x, req_y):
        def get_vector_between_points(x1, y1,x2, y2):
            return np.array([x1-x2, y1-y2])
        def get_direction_vector_pose(theta):
            return np.array([np.cos(theta), np.sin(theta)])
        def unit_vector(vector):
            return vector / np.linalg.norm(vector)

        def get_angle_between_vectors(v1, v2):
            v1_u = unit_vector(v1)
            v2_u = unit_vector(v2)
            return float(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))
        
        def get_signed_angle_between_vectors(v1, v2):
            v1_u = unit_vector(v1)
            v2_u = unit_vector(v2)
            angle = np.arctan2(v2_u[1], v2_u[0]) - np.arctan2(v1_u[1], v1_u[0])
            return angle
        
        def get_signed_angle_with_x_axis(vector):
            return np.arctan2(vector[1], vector[0])
    
        vector_1_to_2 = np.array([req_x - tur_x, req_y - tur_y])
        self.get_logger().info("turtle position: x=" + str())
        angle = get_signed_angle_with_x_axis(vector_1_to_2)

        goal_msg = RotateAbsolute.Goal()
        goal_msg.theta = angle
        self.__rotate_absolute_action_client.wait_for_server()
        self.__rotate_absolute_action_client.send_goal_async(goal_msg)
        return angle
    
    def get_distance_points(self, x1, y1, x2, y2):
        return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def main():
    rclpy.init()

    minimal_service = ComputeTrajectoryService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()