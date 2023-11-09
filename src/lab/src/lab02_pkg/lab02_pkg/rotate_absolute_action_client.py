import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

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




class RotateAbsoluteActionClient(Node):

    def __init__(self):
        super().__init__('rotate_absolute_action_client')
        self._action_client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')
        self.result = None

    def send_goal(self, theta):
        goal_msg = RotateAbsolute.Goal()
        goal_msg.theta = theta

        self._action_client.wait_for_server()
        self.get_logger().info('34')

        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self.get_logger().info('37')

        self._send_goal_future.add_done_callback(self.goal_response_callback)
        self.get_logger().info('40')


    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.result = result
        self.get_logger().info('Result: {0}'.format(result.delta))
        #rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)

    action_client = RotateAbsoluteActionClient()

    action_client.send_goal(float(1.9))

    rclpy.spin(action_client)

    # After spin, we can check if we received the result
    if action_client.result is not None:
        print('Action complete, result:', action_client.result)
    else:
        print('Action did not complete or was not received.')

    rclpy.shutdown()  # Ensure we shutdown after checking the result


if __name__ == '__main__':
    main()