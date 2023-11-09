import time


import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist 
from lab02_interfaces.action import MoveDistance

class MoveDistanceActionServer(Node):

    def __init__(self):
        super().__init__('move_distance')

        action_server_cb_group = ReentrantCallbackGroup()
        subscription_cb_group = MutuallyExclusiveCallbackGroup()

        self.__action_server = ActionServer(
            self,
            MoveDistance,
            'move_distance',
            self.move_distance_callback, 
            callback_group=action_server_cb_group)
        
        self.__turtle_pose_subscription = self.create_subscription(Pose, '/turtle1/pose', self.turtle_pose_subscriber_callback, 10, callback_group=subscription_cb_group)

        self.__turtle_cmd_publisher = self.create_publisher(Twist, "turtle1/cmd_vel", 10)

        self.__turtle_cmd_vel_timer = self.create_timer(0.1, self.turtle_cmd_vel_timer_callback)

        self.turtle_cmd_velocity = 0.0
        self.turtle_pose = Pose()
        self.turtle_moved_distance = 0
        self.time_of_started_action = 0


    def turtle_pose_subscriber_callback(self, msg):
        self.turtle_pose = msg
        return
    
    def turtle_cmd_vel_timer_callback(self):
        msg = Twist()
        msg.linear.x = float(self.turtle_cmd_velocity)
        if msg.linear.x != 0:
            self.__turtle_cmd_publisher.publish(msg)
        self.turtle_moved_distance += (self.turtle_cmd_velocity / 10)
        self.get_logger().info("turtle moved=" + str(self.turtle_moved_distance))

        return

    def move_distance_callback(self, goal_handle):
        self.setpoint_moved_distance = goal_handle.request.distance
        self.turtle_moved_distance = 0
        self.goal_handle = goal_handle
        self.feedback_timer = self.create_timer(0.2, self.feedback_timer_callback)

        time_of_started_action = time.time()

        while abs(self.turtle_moved_distance - self.setpoint_moved_distance) > 0.1:
            self.turtle_cmd_velocity = 0.5
        self.turtle_cmd_velocity = 0
            
        self.feedback_timer.destroy()

        goal_handle.succeed()

        result = MoveDistance.Result()
        result.elapsed_time_s = time.time() - time_of_started_action
        result.traveled_distance = self.turtle_moved_distance
        
        self.turtle_cmd_velocity = 0.0
        self.turtle_pose = Pose()
        self.turtle_moved_distance = 0
        self.time_of_started_action = 0

        return result

    def feedback_timer_callback(self):
        feedback_msg = MoveDistance.Feedback()
        feedback_msg.remaining_distance = self.setpoint_moved_distance - self.turtle_moved_distance
        self.goal_handle.publish_feedback(feedback_msg)




def main(args=None):
    rclpy.init()
    node = MoveDistanceActionServer()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        node.get_logger().info('Beginning client, shut down with CTRL-C')
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt, shutting down.\n')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()