import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, Node, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    ld = LaunchDescription()
    
    ld.add_action(
        DeclareLaunchArgument(
            name='robot_name',
            default_value='robot0'
        )
    )

    ld.add_action(Node(
        package="wheeltec_robot_rc",
        executable="turtlebot_teleop_keyboard",
        name="teleop",
        namespace=f'{LaunchConfiguration('robot_name')}'
    ))

    return ld
