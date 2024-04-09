from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def launch_setup(context, *args, **kwargs):
    parameters=[{
        #   'frame_id': LaunchConfiguration('namespace').perform(context)[1:] + '_link',
          'frame_id': '_link',
          'subscribe_depth':True,
          'approx_sync':True, # Set to True for OAK-D
          'approx_sync_max_interval':  0.01,
          'wait_for_transform': 0.3,
          'feature' : 6,
          'strategy' : 1,
          'nn' : 3
}]

    remappings=[
          ('rgb/image', LaunchConfiguration('namespace').perform(context) + 'camera/color/image_raw'),
          ('rgb/camera_info', LaunchConfiguration('namespace').perform(context) + 'camera/depth/camera_info'),
          ('depth/image', LaunchConfiguration('namespace').perform(context) + 'camera/depth/image_raw'),
          ('odom', LaunchConfiguration('namespace').perform(context) + 'odom'),]

    return [
        # Nodes to launch
        Node(
            package='rtabmap_odom', executable='rgbd_odometry', output='screen', name='rgbd_odometry',
            parameters=parameters,
            remappings=remappings,
            ),
    ]

def generate_launch_description():
    
    return LaunchDescription([            
        # DeclareLaunchArgument('namespace', default_value='/r0',
        #                       description=''),
        DeclareLaunchArgument('namespace', default_value='',
                              description=''),
        OpaqueFunction(function=launch_setup)
    ])
