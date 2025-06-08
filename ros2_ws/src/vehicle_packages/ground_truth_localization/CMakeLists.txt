cmake_minimum_required(VERSION 3.5)
project(ground_truth_localization)

# Add dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2_ros REQUIRED)

# Include directories
include_directories(include)

# Add the executable
add_executable(publish_tf src/publish_tf.cpp)
ament_target_dependencies(publish_tf rclcpp nav_msgs tf2_ros)

# Install the executable
install(TARGETS
  publish_tf
  DESTINATION lib/${PROJECT_NAME})

# Install launch files
install(DIRECTORY
    launch
    DESTINATION share/${PROJECT_NAME}
)

# Finalize
ament_package()