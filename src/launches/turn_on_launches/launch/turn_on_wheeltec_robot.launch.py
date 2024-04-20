import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription, GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from launch_ros.actions import Node, PushRosNamespace


def generate_launch_description():
    ld = LaunchDescription()
    
    ld.add_action(
        DeclareLaunchArgument(
            name='robot_name',
            default_value='robot0'
        )
    )

    ld.add_action(
        DeclareLaunchArgument(
            name='car_mode',
            default_value='mini_tank',
    #    doc="opt: mini_akm,senior_akm,top_akm_bs,top_akm_dl,
    #              mini_mec,senior_mec_bs,senior_mec_dl,top_mec_bs,top_mec_dl,senior_mec_EightDrive,top_mec_EightDrive,
    #              flagship_mec_bs,flagship_mec_dl,
    #              mini_omni,senior_omni,top_omni,
    #              mini_4wd,senior_4wd_bs,senior_4wd_dl,top_4wd_bs,top_4wd_dl,flagship_4wd_bs,flagship_4wd_dl,
    #              mini_tank,mini_diff,senior_diff,four_wheel_diff_bs,four_wheel_diff_dl,flagship_four_wheel_diff_dl,flagship_four_wheel_diff_bs, 
    #              brushless_senior_diff, B585_balance
    #              mini_tank_moveit_four,mini_4wd_moveit_four,mini_mec_moveit_four,
    #              mini_mec_moveit_six,mini_4wd_moveit_six"
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
    # car_mode = 'mini_mec_moveit_six'
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

    ld.add_action(
        Node(
            package='ls01',
            executable='lsn10',
            name='lsn10',
            # emulate_tty=True, output='screen',
            namespace=LaunchConfiguration('robot_name'),
            # parameters=[
            #     {'usart_port_name' : '/dev/wheeltec_controller'},
            # ]
        )
    )
    

    ##### ASTRA

    # launch2 = GroupAction([    
    #    PushRosNamespace(LaunchConfiguration('robot_name')),
    #     IncludeLaunchDescription(
    #                     XMLLaunchDescriptionSource([os.path.join(
    #                     get_package_share_directory('astra_camera'), 'launch/'),
    #                     'astra.launch.xml']), 
    #                 )]
    # )
    
    # ld.add_action(launch2)
    
    ##### RTABMAP

    # rtabmap_args = {
    #     'namespace' : LaunchConfiguration('robot_name')
    # }.items()

    # rtabmap_launch = GroupAction([    
    #     PushRosNamespace(LaunchConfiguration('robot_name')),
    #     IncludeLaunchDescription(
    #                     PythonLaunchDescriptionSource([os.path.join(
    #                     get_package_share_directory('turn_on_launches'), ''),
    #                     'rtabmap_astra_rgbd.launch.py']), 
    #                     # launch_arguments=rtabmap_args
    #                 )]
    # )
    
    # ld.add_action(rtabmap_launch)
    
    ###### ZED 2i
    robot_name = LaunchConfiguration('robot_name')

    zed2i_launch_args = {
            'camera_name' : f"{robot_name}/zed2i",
            'publish_tf' : 'True',
            'camera_model' : 'zed2i',
        }.items()
    
    zed2i_launch = IncludeLaunchDescription(
                        PythonLaunchDescriptionSource([os.path.join(
                        get_package_share_directory('zed_wrapper'), 'launch'),
                        'zed_camera.launch.py']), 
                        launch_arguments=zed2i_launch_args
                    )
    
    ld.add_action(zed2i_launch)
    

    ld.add_action(
        Node(
            package='robot_models_tf2',
            executable='tank',
            name='tank_tf_publisher',
            # emulate_tty=True, output='screen',
            namespace=LaunchConfiguration('robot_name'),
            # parameters=[
            #     {'usart_port_name' : '/dev/wheeltec_controller'},
            # ]
        )
    )

    if ((car_mode == 'mini_mec_moveit_six' or car_mode == 'mini_4wd_moveit_six') and if_voice == 'true'):
        launch_args1 = {
            'odom_frame_id' : LaunchConfiguration('odom_frame_id'),
            'robot_name' : LaunchConfiguration('robot_name'),
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
                'robot_name': LaunchConfiguration('robot_name'),
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
                'robot_name' : LaunchConfiguration('robot_name'),
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
            'robot_name' : LaunchConfiguration('robot_name'),
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
            'robot_name' : LaunchConfiguration('robot_name'),
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
            'robot_name' : LaunchConfiguration('robot_name'),
            }.items()
        
        robot_pose_ekf = IncludeLaunchDescription(
                                        PythonLaunchDescriptionSource([os.path.join(
                                        get_package_share_directory('turn_on_launches'), ''),
                                        '/robot_pose_ekf.launch.py']), 
                                        launch_arguments=args
                                    )
        ld.add_action(robot_pose_ekf)
    
    
    return ld
