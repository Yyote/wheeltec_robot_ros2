import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    ld.add_action(
        DeclareLaunchArgument(
            name='robot_name',
            default_value='r0'
        )
    )

    ld.add_action(
        DeclareLaunchArgument(
            name='odom_frame_id',
            default_value='odom_combined'
        )
    )
    
    ld.add_action(
        DeclareLaunchArgument(
            name='smoother',
            default_value='false'
        )
    )
    
    if LaunchConfiguration('smoother'):
        ld.add_action(
            Node(
                package='turn_on_wheeltec_robot',
                executable='wheeltec_robot_node',
                name='wheeltec_robot',
                namespace=LaunchConfiguration('robot_name'),
                # emulate_tty=True, output='screen',
                parameters=[
                    {'usart_port_name' : '/dev/ttyACM0'},
                    {'serial_baud_rate' : 115200},
                    {'odom_frame_id' : LaunchConfiguration('odom_frame_id')},
                    {'robot_frame_id' : 'base_footprint'},
                    {'gyro_frame_id' : 'gyro_link'}
                ],
                remappings=[('smoother_cmd_vel', 'cmd_vel')]
            )
        )
        
        launch = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('turn_on_launches'), 'launch/include'),
                '/base_serial.launch.py']), 
            )
    else:
        ld.add_action(
            Node(
                package='turn_on_wheeltec_robot',
                executable='wheeltec_robot_node',
                name='wheeltec_robot',
                # emulate_tty=True, output='screen',
                namespace=LaunchConfiguration('robot_name'),
                parameters=[
                    {'usart_port_name' : '/dev/wheeltec_controller'},
                    {'serial_baud_rate' : 115200},
                    {'odom_frame_id' : LaunchConfiguration('odom_frame_id')},
                    {'robot_frame_id' : 'base_footprint'},
                    {'gyro_frame_id' : 'gyro_link'}
                ]
            )
        )
    
    return ld
