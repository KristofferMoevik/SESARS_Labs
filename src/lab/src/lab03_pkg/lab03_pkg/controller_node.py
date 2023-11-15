from sensor_msgs.msg import PointCloud2, LaserScan
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from std_srvs.srv import Empty
from std_msgs.msg import Header

import tf_transformations
import laser_geometry.laser_geometry as lg
import sensor_msgs_py.point_cloud2 as pc2
import rclpy
from rclpy.node import Node
import math
import numpy as np

from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup
from rcl_interfaces.msg import ParameterDescriptor

def create_point_cloud2(points, frame_id="base_link"):
    """ Create a PointCloud2 message from a list of points. """
    header = Header(frame_id=frame_id)  # Set the frame id
    fields = [
        pc2.PointField(name="x", offset=0, datatype=pc2.PointField.FLOAT32, count=1),
        pc2.PointField(name="y", offset=4, datatype=pc2.PointField.FLOAT32, count=1),
        pc2.PointField(name="z", offset=8, datatype=pc2.PointField.FLOAT32, count=1)
    ]
    # Create a PointCloud2 message
    point_cloud_msg = pc2.create_cloud(header, fields, points)
    return point_cloud_msg


def remove_points_behind_robot(point_cloud_msg):
        # List to store filtered points
    filtered_points = []

    # Iterate through points in the PointCloud2 message
    for point in pc2.read_points(point_cloud_msg, skip_nans=False, field_names=("x", "y", "z")):
        x = point[0]
        y = point[1]
        z = point[2]
        if x > 0:
            # Add point to the list if x > 0
            filtered_points.append(point)

    # Create new PointCloud2 message with filtered points
    point_cloud_only_points_front = create_point_cloud2(filtered_points, frame_id=point_cloud_msg.header.frame_id)

    return point_cloud_only_points_front


def find_point_furthest_away_from_robot(point_cloud_msg):
    point_furthest_away = np.array([0,0,0])
    for point in pc2.read_points(point_cloud_msg, skip_nans=False, field_names=("x", "y", "z")):
        if point[0]
        y = point[1]
        z = point[2]
        point_vector = np.array([point[0], point[1], point[2]])
        if np.linalg.norm(point_vector) > np.linalg.norm(point_furthest_away):
            point_furthest_away = point_vector
        

    # Create new PointCloud2 message with filtered points
    point_cloud_point_furthest_away = create_point_cloud2([point_furthest_away.tolist()], frame_id=point_cloud_msg.header.frame_id)

    return point_cloud_point_furthest_away


def find_point_closest_to_robot(point_cloud_msg, angle_threshold=math.pi/4):
    point_closest = np.array([np.inf,np.inf,np.inf])
    for point in pc2.read_points(point_cloud_msg, skip_nans=True, field_names=("x", "y", "z")):
        point_vector = np.array([point[0], point[1], point[2]])
        if abs(np.arctan2(point[1], point[0])) > angle_threshold:
                continue
        if np.linalg.norm(point_vector) < np.linalg.norm(point_closest):
            point_closest = point_vector

    # Create new PointCloud2 message with filtered points
    point_cloud_point_furthest_away = create_point_cloud2([point_closest.tolist()], frame_id=point_cloud_msg.header.frame_id)

    return point_cloud_point_furthest_away        


def get_direction_off_point_furthest_away_from_robot(point_cloud_msg):
    point = pc2.read_points(point_cloud_msg, skip_nans=True, field_names=("x", "y", "z"))[0]
    if point[1] > 0:
        return "left"
    else:
        return "right"


def get_distance_to_closest_point(point_cloud_msg):
        point = np.array([
                pc2.read_points(point_cloud_msg, skip_nans=True, field_names=("x", "y", "z"))[0][0], 
                pc2.read_points(point_cloud_msg, skip_nans=True, field_names=("x", "y", "z"))[0][1], 
                pc2.read_points(point_cloud_msg, skip_nans=True, field_names=("x", "y", "z"))[0][2]])
        return float(np.linalg.norm(point))


def add_angles(angle1, angle2):
    # Convert angles to unit vectors
    sum_angles = angle1 + angle2
    if sum_angles > math.pi:
        sum_angles = sum_angles - 2*math.pi
    if sum_angles < -math.pi:
        sum_angles = sum_angles + 2*math.pi

    return sum_angles

def angle_between_two_angles(angle1, angle2):
    # Convert angles to unit vectors
    vector1 = (math.cos(angle1), math.sin(angle1))
    vector2 = (math.cos(angle2), math.sin(angle2))

    # Compute the dot product
    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

    # Compute the angle between the two vectors
    angle = math.acos(dot_product)

    return angle

class Controller(Node):

        def __init__(self):
                super().__init__('turtlebot3_controller')
                subscribers_cb_group = MutuallyExclusiveCallbackGroup()
                publishers_cb_group = MutuallyExclusiveCallbackGroup()
                controller_cb_group = MutuallyExclusiveCallbackGroup()
                self.laser_scan_subscriber = self.create_subscription(LaserScan, '/scan', self.laser_scan_callback, 10, callback_group=subscribers_cb_group)
                self.odometry_subscriber = self.create_subscription(Odometry, '/diff_drive_controller/odom', self.odometry_callback, 10, callback_group=subscribers_cb_group)
                self.cmd_velocity_publisher = self.create_publisher(Twist, '/cmd_vel', 10, callback_group=publishers_cb_group)
                self.point_cloud_publisher = self.create_publisher(PointCloud2, '/point_cloud', 10, callback_group=publishers_cb_group)
                self.point_cloud_point_furthest_away_publisher = self.create_publisher(PointCloud2, '/point_cloud_point_furthest_away', 10, callback_group=publishers_cb_group)
                self.point_cloud_point_closest_publisher = self.create_publisher(PointCloud2, '/point_cloud_point_closest', 10, callback_group=publishers_cb_group)
                self.direction_of_furthest_away_point_publisher = self.create_publisher(String, '/direction_of_furthest_away_point', 10, callback_group=publishers_cb_group)
                self.controller_loop = self.create_timer(0.1, self.controller_callback, callback_group=controller_cb_group)
                self.laser_projector = lg.LaserProjection()

                # PARAMETERS
                speed_parameter_descriptor = ParameterDescriptor(description='This parameter sets the speed in m/s')
                self.declare_parameter('speed_parameter', 0.5, speed_parameter_descriptor)

                turn_speed_parameter_descriptor = ParameterDescriptor(description='This parameter sets the turning speed')
                self.declare_parameter('turn_speed_parameter', 0.2, speed_parameter_descriptor)

                close_to_wall_threshold_parameter_descriptor = ParameterDescriptor(description='This parameter sets the speed in m/s')
                self.declare_parameter('close_to_wall_threshold', 0.5, speed_parameter_descriptor)

                self.odometry = Odometry()
                self.close_to_wall = False
                self.state = "GO FORWARD"
                self.turning_setpoint = None
                self.distance_to_closest_point = None

        def laser_scan_callback(self, msg):
                laser_scan = msg
                laser_scan_max_range = laser_scan.range_max
                for index, distance in enumerate(laser_scan_msg.ranges):
                        if distance == float('inf'):
                                laser_scan.ranges[index] = laser_scan_max_range
                point_cloud = self.laser_projector.projectLaser(laser_scan)
                point_cloud_only_front = remove_points_behind_robot(point_cloud)
                point_closest_to_robot = find_point_closest_to_robot(point_cloud_only_front, angle_threshold=math.pi/4)
                point_furthest_away = find_point_furthest_away_from_robot(point_cloud_only_front)

                self.point_cloud_publisher.publish(point_cloud_only_front)
                self.point_cloud_point_furthest_away_publisher.publish(point_furthest_away)
                self.point_cloud_point_closest_publisher.publish(point_closest_to_robot)
                self.direction_of_furthest_away_point = get_direction_off_point_furthest_away_from_robot(point_furthest_away)
                self.direction_of_furthest_away_point_publisher.publish(String(data=self.direction_of_furthest_away_point))

                self.distance_to_closest_point = get_distance_to_closest_point(point_closest_to_robot)

                if self.distance_to_closest_point < self.get_parameter('close_to_wall_threshold').value:
                        self.close_to_wall = True
                else:
                        self.close_to_wall = False

        def odometry_callback(self, msg):
                self.odometry = msg    

        def controller_callback(self):
                speed = float(self.get_parameter('speed_parameter').value)
                turn_speed = float(self.get_parameter('turn_speed_parameter').value)
                if self.state == "GO FORWARD":
                        self.get_logger().info(self.state)
                        self.cmd_velocity_publisher.publish(Twist(linear=Vector3(x=speed)))
                        if self.close_to_wall:
                                self.cmd_velocity_publisher.publish(Twist(linear=Vector3(x=0.0)))
                                self.state = "GO BACKWARDS"
                if self.state == "GO BACKWARDS":
                        self.get_logger().info(self.state)
                        self.cmd_velocity_publisher.publish(Twist(linear=Vector3(x=-speed)))
                        if self.distance_to_closest_point > self.get_parameter('close_to_wall_threshold').value + 0.2:
                                self.cmd_velocity_publisher.publish(Twist(linear=Vector3(x=0.0)))
                                self.state = "TURN"
                if self.state == "TURN":
                        self.get_logger().info(self.state)
                        if self.direction_of_furthest_away_point == "left":
                                quat = [self.odometry.pose.pose.orientation.x, self.odometry.pose.pose.orientation.y, self.odometry.pose.pose.orientation.z, self.odometry.pose.pose.orientation.w]
                                _, _, yaw = tf_transformations.euler_from_quaternion(quat)
                                self.turning_setpoint = add_angles(yaw, math.pi/2)
                                self.state = "TURNING LEFT"
                                self.cmd_velocity_publisher.publish(Twist(angular=Vector3(z=turn_speed)))
                        if self.direction_of_furthest_away_point == "right":
                                quat = [self.odometry.pose.pose.orientation.x, self.odometry.pose.pose.orientation.y, self.odometry.pose.pose.orientation.z, self.odometry.pose.pose.orientation.w]
                                _, _, yaw = tf_transformations.euler_from_quaternion(quat)
                                self.turning_setpoint = add_angles(yaw, -math.pi/2)
                                self.state = "TURNING RIGHT"
                                self.cmd_velocity_publisher.publish(Twist(angular=Vector3(z=-turn_speed)))
                if self.state == "TURNING LEFT":
                        quat = [self.odometry.pose.pose.orientation.x, self.odometry.pose.pose.orientation.y, self.odometry.pose.pose.orientation.z, self.odometry.pose.pose.orientation.w]
                        _, _, yaw = tf_transformations.euler_from_quaternion(quat)
                        self.get_logger().info(self.state + "   yaw:" + str(yaw) + "   yawsetpoint:" + str(self.turning_setpoint))
                        self.cmd_velocity_publisher.publish(Twist(angular=Vector3(z=turn_speed)))
                        if 0.01 > abs(angle_between_two_angles(yaw, self.turning_setpoint)):
                                self.state = "GO FORWARD"
                                self.cmd_velocity_publisher.publish(Twist(linear=Vector3(x=speed)))
                if self.state == "TURNING RIGHT":
                        quat = [self.odometry.pose.pose.orientation.x, self.odometry.pose.pose.orientation.y, self.odometry.pose.pose.orientation.z, self.odometry.pose.pose.orientation.w]
                        _, _, yaw = tf_transformations.euler_from_quaternion(quat)
                        self.get_logger().info(self.state + "   yaw:" + str(yaw) + "   yawsetpoint:" + str(self.turning_setpoint))
                        self.cmd_velocity_publisher.publish(Twist(angular=Vector3(z=-turn_speed)))
                        if 0.01 > abs(angle_between_two_angles(yaw, self.turning_setpoint)):
                                self.state = "GO FORWARD"
                                self.cmd_velocity_publisher.publish(Twist(linear=Vector3(x=speed)))



def main(args=None):
    rclpy.init()
    node = Controller()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        node.get_logger().info('Beginning client, shut down with CTRL-C')
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt, shutting down.\n')
    node.destroy_node()
    rclpy.shutdown()