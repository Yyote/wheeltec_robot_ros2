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
    TankModelTFBroadcaster() : Node("TankModelTFBroadcaster") // инициалзация полей
    {
        timer = this->create_wall_timer(20ms, std::bind(&TankModelTFBroadcaster::timer_callback, this));
        broadcaster = std::make_unique<tf2_ros::TransformBroadcaster>(*this);
    }


    private:
    rclcpp::TimerBase::SharedPtr timer;
    std::unique_ptr<tf2_ros::TransformBroadcaster> broadcaster;
    
    
    void timer_callback() // Сама функция колбэка
    {
        TransformStamped transform;
        transform.header.frame_id = "camera_color_optical_frame";
        transform.header.stamp = this->get_clock()->now();
        transform.child_frame_id = "_link";
        
        transform.transform.translation.x = 0;
        transform.transform.translation.y = 0;
        transform.transform.translation.z = 0;

        // transform.transform.rotation.x = 0.5;
        // transform.transform.rotation.y = -0.5;
        // // transform.transform.rotation.z = -0.707;
        // transform.transform.rotation.z = -0.5;
        // // transform.transform.rotation.w = 0.707;
        // transform.transform.rotation.w = -0.5;

        transform.transform.rotation.x = 0;
        transform.transform.rotation.y = 0;
        transform.transform.rotation.z = 0;
        transform.transform.rotation.w = 1;

        broadcaster->sendTransform(transform);
    }
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<TankModelTFBroadcaster>());
    rclcpp::shutdown();
    return 0;
}
