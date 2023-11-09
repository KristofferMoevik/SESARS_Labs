import random 
import math
import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from lab02_interfaces.srv import ComputeTrajectory
from lab02_interfaces.action import MoveDistance
from turtlesim.action import RotateAbsolute

from std_msgs.msg import String
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose


class TurtleGoalNode(Node):

    def __init__(self):
        super().__init__('goal_generator')
        self.__compute_trajectory_service_client = self.create_client(ComputeTrajectory, '/turtle1/compute_trajectory')
        while not self.__compute_trajectory_service_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.__rotate_abs_action_client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')
        self.__move_forward_action_client = ActionClient(self, MoveDistance, '/move_distance')
        self.get_logger().info("Node initialized")

        self.generate_goals_loop()


    def generate_goals_loop(self):
        while True:
            # Create a goal
            goal = self.get_a_goal()
            self.get_logger().info("Created goal: x=" + str(goal.x) + ", y=" + str(goal.y) + ", theta=" + str(goal.theta))

            # Get the trajectory to follow
            req = ComputeTrajectory.Request()
            req.x = goal.x
            req.y = goal.y
            future = self.__compute_trajectory_service_client.call_async(req)
            rclpy.spin_until_future_complete(self, future)
            trajectory = future.result()
            self.get_logger().info("Got trajectory: distance=" + str(trajectory.distance) + ", direction=" + str(trajectory.direction))

            # Rotate the turtle
            rotate_goal = RotateAbsolute.Goal()
            rotate_goal.theta = trajectory.direction
            self.__rotate_abs_action_client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')
            self.__rotate_abs_action_client.wait_for_server()
            future = self.__rotate_abs_action_client.send_goal_async(rotate_goal)

            rclpy.spin_until_future_complete(action_client, future)
            time.sleep(6)

            # Move the turtle to the goal
            move_goal = MoveDistance.Goal()
            move_goal.distance = trajectory.distance
            self.__move_forward_action_client.wait_for_server()
            future = self.__move_forward_action_client.send_goal_async(move_goal)
            rclpy.spin_until_future_complete(self, future)
            moved = future.result()
            self.get_logger().info("Moved turtle distance: x=" + str(move_goal.distance))

            time.sleep(6)

            # Rotate the turtle
            rotate_goal = RotateAbsolute.Goal()
            rotate_goal.theta = goal.theta
            self.__rotate_abs_action_client.wait_for_server()
            future = self.__rotate_abs_action_client.send_goal_async(rotate_goal)
            rclpy.spin_until_future_complete(self, future)
            rotated = future.result()
            self.get_logger().info("Rotated turtle to angle: theta=" + str(rotate_goal.theta))

            time.sleep(6)


    def get_a_goal(self):
        goal_pose = Pose()
        goal_pose.x = float(random.randrange(int(0), int(11)))
        goal_pose.y = float(random.randrange(int(0), int(11)))
        goal_pose.theta = float(random.randint(-3, 3))

        return goal_pose

def main(args=None):
    rclpy.init(args=args)

    controller = TurtleGoalNode()

    rclpy.spin(controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
