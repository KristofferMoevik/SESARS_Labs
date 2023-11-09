import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from turtlesim.action import RotateAbsolute

class TurtleRotateClient(Node):

    def __init__(self):
        super().__init__('turtle_rotate_client')
        self._action_client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')

    def send_goal(self, theta):
        goal_msg = RotateAbsolute.Goal()
        goal_msg.theta = theta

        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

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
        self.get_logger().info(f'Rotation completed: {result.delta:.2f} radians')
        # Shutdown after receiving a response
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)

    turtle_rotate_client = TurtleRotateClient()

    # Send a goal of 1.57 radians (90 degrees)
    turtle_rotate_client.send_goal(1.57)

    # Spin until the action is completed
    rclpy.spin(turtle_rotate_client)

if __name__ == '__main__':
    main()
