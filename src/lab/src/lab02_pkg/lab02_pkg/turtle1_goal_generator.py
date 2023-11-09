#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.service import Service

from lab02_interfaces.srv import ComputeTrajectory
from lab02_interfaces.action import MoveDistance
from turtlesim.action import RotateAbsolute

from turtlesim.msg import Pose
import random
import math

class GoalGenerator(Node):
    def __init__(self):
        super().__init__('goal_generator')
        self.get_logger().info("Goal Generator Node has been started.")
        
        self.compute_trajectory_client = self.create_client(ComputeTrajectory, '/turtle1/compute_trajectory')
        self.move_distance_client = ActionClient(self, MoveDistance, '/turtle1/move_distance')
        self.rotate_absolute_client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')

        self.generate_and_execute_goal()

    def generate_and_execute_goal(self):
        goal_pose = Pose()
        goal_pose.x = random.uniform(0.0, 11.0)
        goal_pose.y = random.uniform(0.0, 11.0)
        goal_pose.theta = random.uniform(0.0, 2*math.pi)
        self.get_logger().info(f"Generated Goal Pose: {goal_pose}")

        self.call_compute_trajectory(goal_pose)

    def call_compute_trajectory(self, goal_pose):
        while not self.compute_trajectory_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('/turtle1/compute_trajectory service not available, waiting again...')
        
        request = ComputeTrajectory.Request()
        request.x = goal_pose.x
        request.y = goal_pose.y
        future = self.compute_trajectory_client.call_async(request)
        future.add_done_callback(self.handle_compute_trajectory_response)

    def handle_compute_trajectory_response(self, future):
        response = future.result()
        if not response:
            self.get_logger().error('Failed to call service /turtle1/compute_trajectory')
            return
        
        # Assuming response contains fields for new orientation and distance to travel
        self.perform_motion(response.direction, response.distance)

    def perform_motion(self, new_orientation, distance_to_travel):
        # Rotate
        rotate_goal = RotateAbsolute.Goal()
        rotate_goal.theta = new_orientation
        self.rotate_absolute_client.wait_for_server()
        self.send_goal_future = self.rotate_absolute_client.send_goal_async(rotate_goal)
        self.send_goal_future.add_done_callback(self.after_rotation)

        # Distance will be moved after rotation is completed in the after_rotation callback.

    def after_rotation(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Rotate goal rejected')
            return

        self.get_logger().info('Rotate goal accepted')

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.start_moving_distance)

    def start_moving_distance(self, future):
        status = future.result().status
        if status != RotateAbsolute.GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().error('Rotation failed')
            return

        self.get_logger().info('Rotation succeeded, moving distance')

        # Move
        move_goal = MoveDistance.Goal()
        move_goal.distance = self.distance_to_travel
        self.move_distance_client.wait_for_server()
        self.send_goal_future = self.move_distance_client.send_goal_async(move_goal)
        self.send_goal_future.add_done_callback(self.after_moving_distance)

    def after_moving_distance(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Move goal rejected')
            return

        self.get_logger().info('Move goal accepted')

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.motion_complete)

    def motion_complete(self, future):
        status = future.result().status
        if status != MoveDistance.GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().error('Moving distance failed')
            return

        self.get_logger().info('Moving distance succeeded')
        self.generate_and_execute_goal()  # Generate a new goal after completing the motion

def main(args=None):
    rclpy.init(args=args)
    goal_generator = GoalGenerator()
    rclpy.spin(goal_generator)
    rclpy.shutdown()

if __name__ == '__main__':
    main()