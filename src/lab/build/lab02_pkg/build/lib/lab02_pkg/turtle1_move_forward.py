import rclpy
from rclpy.node import Node
import rclpy.logging
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup, MutuallyExclusiveCallbackGroup
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from rcl_interfaces.msg import ParameterDescriptor

from lab02_interfaces.action import MoveDistance
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist



class MoveDistanceActionServer(Node):
    def __init__(self):
        super().__init__("move_distance_action_server")

        # CALLBACK GROUPS
        # Define a new callback group for the action server.
        # The action server will be assigned to this group, while the subscribers, publishers and
        # timers will be assigned to the default callback group (which is MutuallyExclusive)
        self.action_server_group = ReentrantCallbackGroup()
        self.topic_group = MutuallyExclusiveCallbackGroup()
        self.timer_group = ReentrantCallbackGroup()

        # SUBSCRIBERS, PUBLISHERS, TIMERS...
        # Subscribers and publishers can stay in the default group since they are non-blocking, to 
        # do so just declare them as usual.
        #
        # You can also assign them explicitely to a MutuallyExclusiveCallbackGroup if you want to by
        # passing the callback_group argument.
        self.pose_subscriber = self.create_subscription(Pose, "pose", self.pose_callback, 10, callback_group=self.topic_group)
        self.cmd_vel_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10, callback_group=self.topic_group)
        self.cmd_vel_timer = self.create_timer(0.1, self.cmd_vel_timer_callback, callback_group=self.timer_group)
        self.feedback_timer = self.create_timer(0.5, self.feedback_timer_callback, callback_group=self.timer_group)

        # The action server must be in a different callback group since it is blocking.
        # The action server callback will sleep at a fixed rate until the goal is completed, failed 
        # or canceled. The action server will use a ReentrantCallbackGroup so that multiple goals 
        # can be handled simultaneously.
        self.action_server = ActionServer(
            self,
            MoveDistance,
            "move_distance",
            self.execute_action_callback,
            callback_group=self.action_server_group,
        )

        # States
        self.pose = Pose()
        self.cmd_vel_msg = Twist()
        self.feedback_msg = MoveDistance.Feedback()
        self.goal_handle = None


        # PARAMETERS
        speed_parameter_descriptor = ParameterDescriptor(description='This parameter sets the speed in m/s')
        self.declare_parameter('speed_parameter', 0.5, speed_parameter_descriptor)

        tolerance_parameter_descriptor = ParameterDescriptor(description='This parameter sets the tolerance of hitting the desired pose')
        self.declare_parameter('tolerance_parameter', 0.2, tolerance_parameter_descriptor)
        
        # This rate object is used to sleep the control loop at a fixed rate in the action server callback
        self.control_rate_hz = 100
        self.control_rate = self.create_rate(self.control_rate_hz)

        self.get_logger().info(
            "Move distance action server has been started, in namespace: "
            + self.get_namespace()
            + " ..."
        )

    def pose_callback(self, msg: Pose):
        self.pose = msg

    def cmd_vel_timer_callback(self):
        if self.goal_handle is not None:
            self.cmd_vel_publisher.publish(self.cmd_vel_msg)

    def feedback_timer_callback(self):
        if self.goal_handle is not None:
            self.goal_handle.publish_feedback(self.feedback_msg)


    def execute_action_callback(self, goal_handle: ServerGoalHandle):
        '''
        This function is called when a new goal is received by the action server.
        Pay attention to return the correct result object, otherwise the action client will crash.
        
        Returns:
            result {YourAction.Result} -- Result object
        '''
        #self.get_logger().info("Executing goal to travel distance: " + str(goal_handle.request.distance) + " m")

        self.feedback_msg = MoveDistance.Feedback()
        result = MoveDistance.Result()
        self.goal_handle = goal_handle

        # Create a condtion to break the control loop, it should be updated at each iteration
        elapsed_time_s = 0.0
        traveled_distance = 0.0

        speed = float(self.get_parameter('speed_parameter').value)
        tolerance = float(self.get_parameter('tolerance_parameter').value)
        
        distance_from_goal = goal_handle.request.distance        
        while True:
            # Execute the control loop at a fixed rate
            self.cmd_vel_msg = Twist()
            self.cmd_vel_msg.linear.x = speed
            #self.get_logger().info("Executing goal with speed: " + str(self.cmd_vel_msg.linear.x) + " and tolerance: " + str(tolerance))
            self.feedback_msg.remaining_distance = distance_from_goal

            elapsed_time_s += 1/self.control_rate_hz
            traveled_distance += speed * (1/self.control_rate_hz)

            self.control_rate.sleep()
            distance_from_goal = goal_handle.request.distance - traveled_distance
            #self.get_logger().info("Distance from goal: " + str(distance_from_goal))
            if (distance_from_goal < tolerance) or (distance_from_goal < 0.0):
                break

        # Result
        result.elapsed_time_s = elapsed_time_s
        result.traveled_distance = traveled_distance

        # Notify the action client that the goal has been completed
        goal_handle.succeed()

        self.goal_handle = None

        return result


def main(args=None):
    rclpy.init(args=args)
    node = MoveDistanceActionServer()
    executor = MultiThreadedExecutor()
    try:
        rclpy.spin(node, executor=executor)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.try_shutdown()