from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    config_path = os.path.join(
        get_package_share_directory('lab02_pkg'),
        'config',
        'parameters.yaml'
    )

    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='',
            executable='turtlesim_node',
            name='turtlesim_node'
        ),
        Node(
            package='lab02_pkg',
            namespace='',
            executable='turtle1_move_forward',
            name='turtle1_move_forward',
            parameters=[config_path]
        ),
        Node(
            package='lab02_pkg',
            namespace='',
            executable='turtle1_compute_trajectory',
            name='turtle1_compute_trajectory'
        ),
        Node(
            package='lab02_pkg',
            namespace='',
            executable='turtle1_goal_node',
            name='turtle1_goal_node',
        ),
        # ExecuteProcess(
        #     cmd=['xterm', '-e', 'ros2 run turtlesim turtle_teleop_key'],
        #     output='screen'
        # ),
    ])
