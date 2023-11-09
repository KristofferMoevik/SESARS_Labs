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
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='turtlesim_node'
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtle_teleop_key',
            name='turtle_teleop_key',
            prefix=["xterm -e"]
        ),
        Node(
            package='lab02_pkg',
            namespace='lab02_pkg',
            executable='turtle1_move_forward',
            name='turtle1_move_forward',
        ),
        Node(
            package='lab02_pkg',
            namespace='lab02_pkg',
            executable='turtle1_goal_generator',
            name='turtle1_goal_generator',
        ),
        Node(
            package='lab02_pkg',
            namespace='lab02_pkg',
            executable='turtle1_compute_trajectory',
            name='turtle1_compute_trajectory'
        )
    ])
