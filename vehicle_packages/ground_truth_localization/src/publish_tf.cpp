#include "rclcpp/rclcpp.hpp"
#include "nav_msgs/msg/odometry.hpp"
#include "message_filters/subscriber.h"
#include "message_filters/sync_policies/approximate_time.h"
#include "message_filters/synchronizer.h"
#include "tf2_ros/transform_broadcaster.h"

class PublishGroundTruthTf : public rclcpp::Node {
public:
    PublishGroundTruthTf() : Node("publish_tf") {
        subscription_ = this->create_subscription<nav_msgs::msg::Odometry>(
            "ground_truth_pose", 10, std::bind(&PublishGroundTruthTf::topic_callback, this, std::placeholders::_1));

        odometry_publisher_ = this->create_publisher<nav_msgs::msg::Odometry>(
            "odom", 10);

        this->declare_parameter("publish_map_to_odom_tf", rclcpp::ParameterValue(true));
        this->get_parameter("publish_map_to_odom_tf", map_to_odom_tf_);

        tf_broadcaster_ = std::make_shared<tf2_ros::TransformBroadcaster>(this);

        current_kf_id_ = 0;
        prev_time = std::chrono::high_resolution_clock::now();
    }

private:

    void topic_callback(nav_msgs::msg::Odometry::SharedPtr msg)
    {
        odometry_publisher_->publish(*msg);
        // RCLCPP_INFO(this->get_logger(), "Received odometry message: x: '%f', y: '%f'", msg->pose.pose.position.x, msg->pose.pose.position.y);
    
        geometry_msgs::msg::TransformStamped transform_stamped;

        // odom to base_link
        transform_stamped.header.stamp = msg->header.stamp;
        transform_stamped.header.frame_id = static_cast<std::string>(this->get_namespace()) + "/odom";
        transform_stamped.child_frame_id = static_cast<std::string>(this->get_namespace()) + "/base_footprint";

        transform_stamped.transform.translation.x = msg->pose.pose.position.x;
        transform_stamped.transform.translation.y = msg->pose.pose.position.y;
        transform_stamped.transform.translation.z = msg->pose.pose.position.z;
        transform_stamped.transform.rotation = msg->pose.pose.orientation;

        tf_broadcaster_->sendTransform(transform_stamped);

        if(map_to_odom_tf_)
        {
            // map to odom (0 transform)
            transform_stamped.header.stamp = msg->header.stamp;
            transform_stamped.header.frame_id = "map";
            transform_stamped.child_frame_id = static_cast<std::string>(this->get_namespace()) + "/odom";

            transform_stamped.transform.translation.x = 0.0;
            transform_stamped.transform.translation.y = 0.0;
            transform_stamped.transform.translation.z = 0.0;
            geometry_msgs::msg::Quaternion default_quat;
            transform_stamped.transform.rotation = default_quat;

            tf_broadcaster_->sendTransform(transform_stamped);
        }
        if(map_to_odom_tf_)
        {
            // map to odom (0 transform)
            transform_stamped.header.stamp = msg->header.stamp;
            transform_stamped.header.frame_id = "map";
            transform_stamped.child_frame_id = static_cast<std::string>(this->get_namespace()) + "/odom";

            transform_stamped.transform.translation.x = 0.0;
            transform_stamped.transform.translation.y = 0.0;
            transform_stamped.transform.translation.z = 0.0;
            geometry_msgs::msg::Quaternion default_quat;
            transform_stamped.transform.rotation = default_quat;

            tf_broadcaster_->sendTransform(transform_stamped);
        }
    }

    std::shared_ptr<tf2_ros::TransformBroadcaster> tf_broadcaster_;
    rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr subscription_;
    rclcpp::Publisher<nav_msgs::msg::Odometry>::SharedPtr odometry_publisher_;
    long unsigned current_kf_id_;
    std::chrono::_V2::system_clock::time_point prev_time;
    bool map_to_odom_tf_;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<PublishGroundTruthTf>());
    rclcpp::shutdown();
    return 0;
}