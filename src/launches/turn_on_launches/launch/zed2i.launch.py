import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node, PushRosNamespace


def generate_launch_description():
    ld = LaunchDescription()
    
    ld.add_action(
        DeclareLaunchArgument(
            name='robot_name',
            default_value='robot0'
        )
    )

    launch_args1 = {
            'camera_name' : LaunchConfiguration('robot_name')+"/zed2i",
            'publish_tf' : True,
            'camera_model' : 'zed2i',
        }.items()
    
    launch1 = IncludeLaunchDescription(
                        PythonLaunchDescriptionSource([os.path.join(
                        get_package_share_directory('turn_on_launches'), ''),
                        '/base_serial.launch.py']), 
                        launch_arguments=launch_args1
                    )
    
    ld.add_action(launch1)

    return ld

