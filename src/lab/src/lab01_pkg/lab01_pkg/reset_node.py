import math

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import Pose 

class Reset(Node):
    # Create a node called /reset_node that subscribes to /pose. When the distance from the
    # origin of the reference frame is larger than 6.0 m, publish a boolean value (True or False, as
    # you wish) on the topic /reset to take care of this limit condition and reset the node.

    def __init__(self):
        super().__init__('reset')
        self.origin = Pose()
        self.origin.position.x = float(0)
        self.origin.position.y = float(0)
        self.origin_reset_threshold = float(6)
        self.pose_subscriber_ = self.create_subscription(Pose, 'pose', self.pose_subscriber_callback, 10)
        self.reset_publisher_ = self.create_publisher(Bool, 'reset', 10)

    def pose_subscriber_callback(self, msg):
        self.dist = math.sqrt((float(msg.position.x) - float(self.origin.position.x))**2 + (float(msg.position.y) - float(self.origin.position.y))**2)
        reset_msg = Bool()
        if self.dist >= 6:
            reset_msg.data = True
            self.reset_publisher_.publish(reset_msg)
            self.get_logger().info("Publishing: Reset = True")
        else:
            reset_msg.data = False
            self.reset_publisher_.publish(reset_msg)
            self.get_logger().info("Publishing: Reset = False")



def main(args=None):
    rclpy.init(args=args)

    reset = Reset()

    rclpy.spin(reset)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    reset.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
