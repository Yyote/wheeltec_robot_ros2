from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    ld = LaunchDescription()
    
    ld.add_action(
        DeclareLaunchArgument(
            name='is_cartographer',
            default_value='false',
        )
    )
    
    
    if not LaunchConfiguration('is_cartographer'):
        ld.add_action(Node(
            package="robot_pose_ekf",
            node_executable="robot_pose_ekf",
            node_name="robot_pose_ekf",
            output="screen",
            parameters=[
                {"output_frame" : "odom_combined"},
                {"base_footprint_frame" : "base_footprint"},
                {"freq" : "30.0"},
                {"sensor_timeout" : "2.0"},
                {"odom_used" : "true"},
                {"imu_used" : "true"},
                {"vo_used" : "false"},
            ],
            remappings=[
                ('imu_data', 'imu')
            ]
        ))
    
    return ld