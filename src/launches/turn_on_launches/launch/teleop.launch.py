from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node


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
        namespace=LaunchConfiguration('robot_name')
    ))

    return ld
