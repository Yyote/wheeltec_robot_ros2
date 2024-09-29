#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "tf2_ros/transform_broadcaster.h"
#include "geometry_msgs/msg/transform_stamped.hpp"


using namespace std::chrono_literals;
using geometry_msgs::msg::TransformStamped;

class TankModelTFBroadcaster : public rclcpp::Node
{
    public:
    TankModelTFBroadcaster() : Node("OmniModelTFBroadcaster") // инициалзация полей
    {
        timer = this->create_wall_timer(20ms, std::bind(&TankModelTFBroadcaster::timer_callback, this));
        broadcaster = std::make_unique<tf2_ros::TransformBroadcaster>(*this);

        std::string default_robot_name = "r0";
        this->declare_parameter("robot_name", default_robot_name);
        this->get_parameter_or("robot_name", robot_name, default_robot_name);
    }


    private:
    rclcpp::TimerBase::SharedPtr timer;
    std::unique_ptr<tf2_ros::TransformBroadcaster> broadcaster;
    std::string robot_name;
    
    
    void timer_callback() // Сама функция колбэка
    {
        TransformStamped base2cam_transform;
        base2cam_transform.header.frame_id = robot_name + "/base_link";
        base2cam_transform.header.stamp = this->get_clock()->now();
        base2cam_transform.child_frame_id = robot_name + "/base_link";
        
        base2cam_transform.transform.translation.x = -0.17;
        base2cam_transform.transform.translation.y = 0.02;
        base2cam_transform.transform.translation.z = 0.05;

        // base2cam_transform.transform.rotation.x = 0.5;
        base2cam_transform.transform.rotation.x = 0;
        base2cam_transform.transform.rotation.y = 0;
        base2cam_transform.transform.rotation.z = 0;
        base2cam_transform.transform.rotation.w = 1;

        broadcaster->sendTransform(base2cam_transform);

        TransformStamped lidar2base_transform;
        lidar2base_transform.header.frame_id = robot_name + "/base_link";
        lidar2base_transform.header.stamp = this->get_clock()->now();
        lidar2base_transform.child_frame_id = robot_name + "/laser";
        
        lidar2base_transform.transform.translation.x = -0.17;
        lidar2base_transform.transform.translation.y = 0.02;
        lidar2base_transform.transform.translation.z = 0.05;

        // lidar2base_transform.transform.rotation.x = 0.5;
        lidar2base_transform.transform.rotation.x = 0;
        lidar2base_transform.transform.rotation.y = 0;
        lidar2base_transform.transform.rotation.z = 0;
        lidar2base_transform.transform.rotation.w = 1;

        broadcaster->sendTransform(lidar2base_transform);
    }
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<TankModelTFBroadcaster>());
    rclcpp::shutdown();
    return 0;
}
