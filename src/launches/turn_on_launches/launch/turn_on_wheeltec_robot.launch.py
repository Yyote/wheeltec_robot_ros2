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

    """
    Here we get the values of the necessary environment variables,
    that users have to set manually accroding to their robot group parameters.
    """
    robot_name = os.getenv('ROBOT_NAME') # This will be used as a prefix in many places like node namespaces, topic prefixes, tf prefixes, etc.
    camera_capabilities = os.getenv('ROBOT_CAMERA_CAPABILITIES') # This defines the pipeline that the robot uses to get pointclouds and visual odometry

    if robot_name is None or camera_capabilities is None:
        raise Exception('Environment variables are not set. Please check the list carefully and set them accordingly.')

    print(f'camera_capabilities: {camera_capabilities}')

    ld.add_action(
        DeclareLaunchArgument(
            name='car_mode',
            default_value='mini_tank',
        )
    )
    ld.add_action(
        DeclareLaunchArgument(
            name='navigation',
            default_value='false'
        )
    )
    ld.add_action(
        DeclareLaunchArgument(
            name='pure3d_nav',
            default_value='false'
        )
    )
    ld.add_action(
        DeclareLaunchArgument(
            name='repeat',
            default_value='false'
        )
    )
    ld.add_action(
        DeclareLaunchArgument(
            name='if_voice',
            default_value='false'
        )
    )
    ld.add_action(
        DeclareLaunchArgument(
            name='is_cartographer',
            default_value='false'
        )
    )
    ld.add_action(
        DeclareLaunchArgument(
            name='odom_frame_id',
            default_value='odom_combined'
        )
    )

    car_mode = LaunchConfiguration('car_mode')
    if_voice = LaunchConfiguration('if_voice')

    if car_mode == 'mini_akm' or car_mode == 'senior_akm' or car_mode == 'top_akm_bs' or car_mode == 'top_akm_dl':
        ld.add_action(
            DeclareLaunchArgument(
                name='if_akm_yes_or_no',
                default_value='yes'
            )
        )
    if car_mode == 'mini_mec_moveit_six' or car_mode == 'mini_4wd_moveit_six':
        ld.add_action(
            DeclareLaunchArgument(
                name='if_six',
                default_value='yes'
            )
        )

    """
    LSN10 lidar launch. More lidars have to be added
    """
    ld.add_action(
        Node(
            package='ls01',
            executable='lsn10',
            name='lsn10',
            # emulate_tty=True, output='screen',
            namespace=robot_name,
            parameters=[
                {'lidar_frame' : robot_name + '/laser'},
            ]
        )
    )
    

    if camera_capabilities == 'astra_s':
        ##### ASTRA
        launch2 = GroupAction([    
            PushRosNamespace(robot_name),
            IncludeLaunchDescription(
                            XMLLaunchDescriptionSource([os.path.join(
                            get_package_share_directory('astra_camera'), 'launch/'),
                            'astra.launch.xml']), 
                        )]
        )
        
        ld.add_action(launch2)

        ##### RTABMAP
        """
        Most probably wont be used because loses navigation too often
        """
        rtabmap_args = {
            'namespace' : robot_name
        }.items()

        rtabmap_launch = GroupAction([    
            PushRosNamespace(robot_name),
            IncludeLaunchDescription(
                            PythonLaunchDescriptionSource([os.path.join(
                            get_package_share_directory('turn_on_launches'), ''),
                            'rtabmap_astra_rgbd.launch.py']), 
                            # launch_arguments=rtabmap_args
                        )]
        )
        
        ld.add_action(rtabmap_launch)

    elif camera_capabilities == 'zed2i':
        ###### ZED 2i
        robot_name = robot_name
        
        zed2i_launch_args = {
                'camera_name' : robot_name,
                'publish_tf' : 'true',
                'camera_model' : 'zed2i',
            }.items()
        
        zed2i_launch = IncludeLaunchDescription(
                            PythonLaunchDescriptionSource([os.path.join(
                            get_package_share_directory('zed_wrapper'), 'launch/'),
                            'zed_camera.launch.py']), 
                            launch_arguments=zed2i_launch_args
                        )
        
        ld.add_action(zed2i_launch)
        
        cslam_args = {
                'namespace' : robot_name,
                'cslam_config_file' : 'zed2i_swarm_slam.yaml',
                'robot_id' : '0'
            }.items()
        
        print('WARNING! CSLAM ARGS CONTAIN HARDCODED VALUE ZERO FOR ROBOT ID!')

        cslam_launch = GroupAction([
            SetRemap(src=f'/{robot_name}/depth/image', dst=f'/{robot_name}/zed_node/depth/image'),
            SetRemap(src=f'/{robot_name}/odom', dst=f'/{robot_name}/zed_node/odom'),
            SetRemap(src=f'/{robot_name}/color/camera_info', dst=f'/{robot_name}/zed_node/rgb/camera_info'),
            SetRemap(src=f'/{robot_name}/color/image', dst=f'/{robot_name}/zed_node/rgb/image_rect_color'),
            SetRemap(src=f'/{robot_name}/left/camera_info', dst=f'/{robot_name}/zed_node/left/camera_info'),
            SetRemap(src=f'/{robot_name}/left/image_rect', dst=f'/{robot_name}/zed_node/left/image_rect_color'),
            SetRemap(src=f'/{robot_name}/right/camera_info', dst=f'/{robot_name}/zed_node/left/camera_info'),
            SetRemap(src=f'/{robot_name}/right/image_rect', dst=f'/{robot_name}/zed_node/left/image_rect_color'),
            IncludeLaunchDescription(
                                PythonLaunchDescriptionSource([os.path.join(
                                get_package_share_directory('turn_on_launches'), ''),
                                'swarm_slam.launch.py']), 
                                launch_arguments=cslam_args
                            ),
        ])
        
        ld.add_action(cslam_launch)

    ld.add_action(
        Node(
            package='robot_models_tf2',
            executable='tank',
            name='tank_tf_publisher',
            # emulate_tty=True, output='screen',
            namespace=robot_name,
            # parameters=[
            #     {'usart_port_name' : '/dev/wheeltec_controller'},
            # ]
        )
    )

    if ((car_mode == 'mini_mec_moveit_six' or car_mode == 'mini_4wd_moveit_six') and if_voice == 'true'):
        launch_args1 = {
            'odom_frame_id' : LaunchConfiguration('odom_frame_id'),
            'robot_name' : robot_name,
            }.items()
        launch1 = IncludeLaunchDescription(
                            PythonLaunchDescriptionSource([os.path.join(
                            get_package_share_directory('turn_on_launches'), ''),
                            '/base_serial.launch.py']), 
                            launch_arguments=launch_args1
                        )
        
        launch_args2 = [
            {
                'if_voice_control' : True,
                'moveit_config' : True,
                'preset' : True,
                'robot_name': robot_name,
                }.items(),
        ]
        launch2 = IncludeLaunchDescription(
                            PythonLaunchDescriptionSource([os.path.join(
                            get_package_share_directory('wheeltec_arm_pick'), 'launch'),
                            '/base_serial.launch.py']), 
                            launch_arguments=launch_args2
                        )
        
        ld.add_action(launch1)
        ld.add_action(launch2)
    
    if not ((car_mode == 'mini_mec_moveit_six' or car_mode == 'mini_4wd_moveit_six') and if_voice == 'true'):
        launch_args2 = {
                'odom_frame_id' : LaunchConfiguration('odom_frame_id'),
                'robot_name' : robot_name,
            }.items()
        launch2 = IncludeLaunchDescription(
                            PythonLaunchDescriptionSource([os.path.join(
                            get_package_share_directory('turn_on_launches'), ''),
                            'base_serial.launch.py']), 
                            launch_arguments=launch_args2
                        )
        
        ld.add_action(launch2)
    
    if LaunchConfiguration('navigation') == 'true':
        args={
            'car_mode' : car_mode,
            'robot_name' : robot_name,
            }.items()
        launch_teb_local_planner = IncludeLaunchDescription(
                                        PythonLaunchDescriptionSource([os.path.join(
                                        get_package_share_directory('turn_on_launches'), 'launch'),
                                        '/teb_local_planner.launch.py']), 
                                        launch_arguments=args
                                    )
        ld.add_action(launch_teb_local_planner)

    if LaunchConfiguration('pure3d_nav') == 'true':
        args={
            'car_mode' : car_mode,
            'robot_name' : robot_name,
            }.items()
        launch_teb_local_planner = IncludeLaunchDescription(
                                        PythonLaunchDescriptionSource([os.path.join(
                                        get_package_share_directory('turn_on_launches'), 'launch'),
                                        '/teb_local_planner_pure3d.launch.py']), 
                                        launch_arguments=args
                                    )
        ld.add_action(launch_teb_local_planner)
    
    if LaunchConfiguration('repeat') != 'true':
        # robot_model_visualization = IncludeLaunchDescription(
        #                                 PythonLaunchDescriptionSource([os.path.join(
        #                                 get_package_share_directory('turn_on_launches'), 'launch'),
        #                                 '/robot_model_visualization.launch.py']), 
        #                                 launch_arguments=[{'car_mode' : car_mode}, {'if_voice' : if_voice}]
        #                             )
        # ld.add_action(robot_model_visualization)
        args={
            'is_cartographer' : LaunchConfiguration('is_cartographer'),
            'robot_name' : robot_name,
            }.items()
        
        robot_pose_ekf = IncludeLaunchDescription(
                                        PythonLaunchDescriptionSource([os.path.join(
                                        get_package_share_directory('turn_on_launches'), ''),
                                        '/robot_pose_ekf.launch.py']), 
                                        launch_arguments=args
                                    )
        ld.add_action(robot_pose_ekf)
    
    
    return ld
