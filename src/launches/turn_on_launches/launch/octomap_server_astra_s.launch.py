import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from launch_ros.actions import Node, PushRosNamespace, SetRemap


def generate_launch_description():
    ld = LaunchDescription()

    ld.add_action(
        Node(
            package='octomap_server2',
            executable='octomap_server',
            # executable='octomap_server_multilayer_node',
            name='octomap_server',
            remappings=[
                ("/cloud_in", "/camera/depth_registered/points")
            ],
            parameters=[
                # {"resolution" : 0.05},
                {"frame_id" : "map"},
                {"base_frame_id" : "camera_link"},
                # {"sensor_model.max_range" : 5.0},
                {"latched" : False},
            ]
        )
    )
        
    return ld
