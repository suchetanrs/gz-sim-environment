#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist_stamped.hpp"
#include "geometry_msgs/msg/twist.hpp"

class TwistConverter : public rclcpp::Node
{
public:
  TwistConverter() : Node("twist_converter")
  {
    // Create a publisher for geometry_msgs::msg::Twist messages.
    twist_pub_ = this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel_nav", 10);

    // Create a subscription to geometry_msgs::msg::TwistStamped messages.
    twist_stamped_sub_ = this->create_subscription<geometry_msgs::msg::TwistStamped>(
      "cmd_vel_nav_stamped",
      10,
      std::bind(&TwistConverter::twistStampedCallback, this, std::placeholders::_1)
    );
  }

private:
  // Callback function to handle incoming TwistStamped messages.
  void twistStampedCallback(const geometry_msgs::msg::TwistStamped::SharedPtr msg)
  {
    // Create a Twist message from the twist field of the incoming TwistStamped message.
    auto twist_msg = geometry_msgs::msg::Twist();
    twist_msg = msg->twist;  // Direct copy of the twist data

    // Publish the Twist message.
    twist_pub_->publish(twist_msg);
  }

  // Publisher for Twist messages.
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr twist_pub_;

  // Subscription for TwistStamped messages.
  rclcpp::Subscription<geometry_msgs::msg::TwistStamped>::SharedPtr twist_stamped_sub_;
};

int main(int argc, char * argv[])
{
  // Initialize ROS 2
  rclcpp::init(argc, argv);

  // Create the TwistConverter node and spin to process callbacks.
  rclcpp::spin(std::make_shared<TwistConverter>());

  // Shutdown ROS 2
  rclcpp::shutdown();
  return 0;
}