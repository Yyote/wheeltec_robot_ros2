from launch_ros.actions import Node
import launch_ros.actions as actions
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    ld = LaunchDescription()
    
    ld.add_action(
        DeclareLaunchArgument(
            name='robot_name',
            default_value='r0'
        )
    )

    ld.add_action(DeclareLaunchArgument(
        name='car_mode',
        default_value=''
    ))

    ld.add_action(DeclareLaunchArgument(
        name='if_voice',
        default_value='false'
    ))

    car_mode = LaunchConfiguration('car_mode')

    ld.add_action(Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        namespace=LaunchConfiguration('robot_name'),
        name='base_to_link',
        arguments=f'0 0 0 0 0 0 base_footprint base_link 100'
    ))
    
# Трансформации
    if car_mode == 'mini_tank':
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.04 0.00 0.21 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.1 0.00 0.16 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
    
    # ЕБАШЬ СЮДА
    # ЕБАШЬ СЮДА
    # ЕБАШЬ СЮДА
    # ЕБАШЬ СЮДА
    # ЕБАШЬ СЮДА
    if car_mode == "mini_akm":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.125 0.00 0.15 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.185 0.00 0.1 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
    ################################################
    if car_mode == "senior_akm":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.26 0.00 0.228 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.34 0.00 0.178 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        ############################################
    if car_mode == "top_akm_bs":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.53 0.00 0.278 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.59 0.00 0.228 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        ##############################################
    if car_mode == "top_akm_dl":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.52 0.00 0.350 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.58 0.00 0.30 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        ##############################################
    if car_mode == "mini_mec":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.06 0.00 0.20 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.12 0 0.15 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        #############################################
    if car_mode == "mini_mec_moveit_four":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.048 0.00 0.18 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'-0.118 0 0.50 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        ##################################################
    if car_mode == "mini_mec_moveit_six":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.048 0.00 0.11 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'-0.118 0 0.55 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        ##########################################################
    if car_mode == "senior_mec_bs":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.12 0.00 0.165 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.18 0 0.115 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        ############################################################
    if car_mode == "senior_mec_dl":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.18 0.00 0.32 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.240 0 0.27 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        #########################################################################
    if car_mode == "top_mec_bs":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.18 0.00 0.32 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.240 0 0.27 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        ##############################################################################
    if car_mode == "top_mec_dl":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.18 0.00 0.32 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.240 0 0.27 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        ###############################################################
    if car_mode == "senior_mec_EightDrive":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.26 0.00 0.23 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.320 0 0.18 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        ####################################################################
    if car_mode == "top_mec_EightDrive":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.26 0.00 0.23 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.320 0 0.18 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))
        #########################################################################
    if car_mode == "flagship_mec_dl":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.20 0.00 0.34 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.240 0 0.27 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))           
        ############################################################################
    if car_mode == "flagship_mec_bs":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.20 0.00 0.34 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.240 0 0.27 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))   
        #########################################################################
    if car_mode == "mini_omni":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.015 0.00 0.17 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.075 0.00 0.12 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))   
        ##############################################################################
    if car_mode == "senior_omni":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.09 0.00 0.25 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.15 0.00 0.20 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))           
        ##################################################################################
    if car_mode == "top_omni":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.18 0.00 0.28 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.24 0.00 0.23 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))             
        #################################################################################
    if car_mode == "mini_4wd":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.06 0.00 0.20 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.12 0 0.15 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))     
        ###############################################################################
    if car_mode == "mini_4wd_moveit_four":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.048 0.00 0.18 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'-0.118 0 0.50 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))  
        ###################################################################################
    if car_mode == "mini_4wd_moveit_six":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.048 0.00 0.18 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'-0.118 0 0.50 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        )) 
        #####################################################################################
    if car_mode == "senior_4wd_bs":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.12 0.00 0.228 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.18 0 0.178 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))            
        ####################################################################################
    if car_mode == "senior_4wd_dl":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.18 0.00 0.36 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.240 0 0.31 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))   
        #####################################################################################
    if car_mode == "top_4wd_bs":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.18 0.00 0.36 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.240 0 0.31 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))   
        #####################################################################################
    if car_mode == "top_4wd_dl":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.18 0.00 0.37 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.240 0 0.32 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))              
        ######################################################################################
    if car_mode == "flagship_4wd_bs":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'-0.05 0.00 0.364 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.01 0.00 0.324 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        )) 
        ###################################################################################################
    if car_mode == "flagship_4wd_dl":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'-0.05 0.00 0.364 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.01 0.00 0.324 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))         
        ################################################################################################
    if car_mode == "mini_tank_moveit_four":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.048 0.00 0.18 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'-0.118 0 0.50 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))   
        ############################################################################################
    if car_mode == "mini_diff":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.125 0.00 0.16 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.185 0.00 0.11 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))             
        #############################################################################
    if car_mode == "senior_diff":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.23 0.00 0.20 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.29 0.00 0.15 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))  
        #################################################################################
    if car_mode == "four_wheel_diff_bs":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'-0.05 0.00 0.36 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.01 0.00 0.31 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))          
        ########################################################################################
    if car_mode == "four_wheel_diff_dl":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'-0.05 0.00 0.36 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.01 0.00 0.31 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        )) 
        #####################################################################################
    if car_mode == "flagship_four_wheel_diff_dl":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'-0.05 0.00 0.36 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.01 0.00 0.31 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))           
        ##########################################################################################
    if car_mode == "flagship_four_wheel_diff_bs":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'-0.05 0.00 0.36 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.01 0.00 0.31 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'0 0 0 0 0 0 base_footprint gyro_link 100'
        ))              
        ###################################################################################################
    if car_mode == "brushless_senior_diff":
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_laser',
            arguments=f'0.036 0.00 0.26 3.14 0 0  base_footprint laser 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_camera',
            arguments=f'0.073 0.00 0.34 0 0 0   base_footprint camera_link 100'
        ))
        ld.add_action(Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace=LaunchConfiguration('robot_name'),
            name='base_to_gyro',
            arguments=f'-0.194 -0.092 0.22 0 0 0 base_footprint gyro_link 100'
        ))      


    # ЕБАШЬ ДО ЮСДА
    # ЕБАШЬ ДО ЮСДА
    # ЕБАШЬ ДО ЮСДА
    # ЕБАШЬ ДО ЮСДА
    # ЕБАШЬ ДО ЮСДА
    # ЕБАШЬ ДО ЮСДА
    # ЭТО КОНЕЦ ТЫ ПИДОР
    
    
# Описание робота
    if car_mode == 'mini_tank':
        ld.add_action(
            DeclareLaunchArgument(
                name='robot_description',
                default_value=f'{os.path.join(get_package_share_directory("turn_on_wheeltec_robot"), "urdf/mini_4wd_robot.urdf")}',
                # description='Описание аргумента'
            )
        )
    
    
    
    return ld