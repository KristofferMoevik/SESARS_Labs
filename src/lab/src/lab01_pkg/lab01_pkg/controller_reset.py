import rclpy
from rclpy.node import Node
from rclpy.logging import LoggingSeverity

from std_msgs.msg import Bool
from geometry_msgs.msg import Twist 

class Controller_Reset(Node):
    # publishes velocities on a topic called
    # /cmd_topic of type ‘geometry_msgs/msg/Twist at a frequency of 1 Hz. The robot
    # always moves at 1 m/s, and its movement follows this rule:
    # 1. N seconds along the X-axis
    # 2. N seconds along the Y-axis
    # 3. N seconds opposite the X-axis
    # 4. N seconds opposite the Y-axis
    # N starts from 1 and increases by 1 after each set of movements

    def __init__(self):
        super().__init__('controller_reset')
        self.vel_publisher_ = self.create_publisher(Twist, 'cmd_topic', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.reset_subscriber_ = self.create_subscription(Bool, 'reset', self.reset_subscriber_callback, 10)
        self.step = 1
        self.N = 1
        self.count_N = 0

    def timer_callback(self):
        
        if self.count_N >= self.N:
            self.count_N = 0
            if self.step < 4:
                self.step += 1
            else:
                self.step = 1
                self.N += 1
                
        msg = Twist()
        if self.step == 1:
            msg.linear.x = float(1)
        elif self.step == 2:
            msg.linear.y = float(1)
        elif self.step == 3:
            msg.linear.x = float(-1)
        elif self.step == 4:
            msg.linear.y = float(-1)
        self.count_N += 1

        self.vel_publisher_.publish(msg)
        self.get_logger().log('Publishing: "%s"' % msg.linear, LoggingSeverity.DEBUG)

    def reset_subscriber_callback(self, msg):
        if msg.data == True:
            self.step = 1
            self.N = 1
            self.count_N = 0
            self.get_logger().info("Controller node has been reset")
            self.timer_callback()




def main(args=None):
    rclpy.init(args=args)

    controller = Controller_Reset()

    rclpy.spin(controller)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
