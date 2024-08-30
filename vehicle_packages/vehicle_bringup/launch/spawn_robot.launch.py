import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchContext, LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro
import subprocess

robot_coordinates = {
    0: [0.0, -1.5, 1.65],
    1: [0.0, 5.0, 1.65],
    2: [5.0, 5.0, 1.65],
    3: [-1.0, 8.0, 1.65],
    4: [7.0, 8.0, 1.65],
    5: [7.0, 8.0, 1.65]
}

robot_model_type = "model"
# you can choose from:
# model, model_with_2_lidar

def spawn_robot(context: LaunchContext, namespace: LaunchConfiguration):
    pkg_project_description = get_package_share_directory("vehicle_bringup")
    robot_ns = namespace.perform(context)
    robot_idx_str = robot_ns[-2]
    robot_idx = int(robot_idx_str)

    erb_file = os.path.join(pkg_project_description, 'models', '4_wheel_differential', robot_model_type + '.erb')
    rb_file = os.path.join(pkg_project_description, 'models', '4_wheel_differential', 'model.rb')
    print(f"ruby {rb_file} {robot_ns} {erb_file} /tmp/model_{robot_idx_str}.sdf {robot_coordinates[robot_idx][0]} {robot_coordinates[robot_idx][1]}")
    process = subprocess.run(f"ruby {rb_file} {robot_ns} {erb_file} /tmp/model_{robot_idx_str}.sdf {robot_coordinates[robot_idx][0]} {robot_coordinates[robot_idx][1]}", shell=True, check=True)
    
    with open(f"/tmp/model_{robot_idx_str}.sdf", 'r') as infp:
        robot_desc = infp.read()

    # Spawn a robot inside a simulation
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        name="ros_gz_sim_create" + robot_idx_str,
        output="both",
        arguments=[
            "-topic",
            "robot_description",
            "-name",
            robot_ns,
            "-x",
            str(robot_coordinates[robot_idx][0]),
            "-y",
            str(robot_coordinates[robot_idx][1]),
            "-z",
            str(robot_coordinates[robot_idx][2]),
        ],
    )

    # Launch robot state publisher node
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher" + robot_idx_str,
        output="both",
        parameters=[
            {"use_sim_time": True},
            {"robot_description": robot_desc},
        ],
    )

    # Bridge ROS topics and Gazebo messages for establishing communication
    topic_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        name="parameter_bridge" + robot_idx_str,
        arguments=[
            robot_ns + "cmd_vel_nav@geometry_msgs/msg/Twist]ignition.msgs.Twist",
            robot_ns + "odom@nav_msgs/msg/Odometry[ignition.msgs.Odometry",
            robot_ns + "ground_truth_pose@nav_msgs/msg/Odometry[ignition.msgs.Odometry",
            robot_ns + "imu@sensor_msgs/msg/Imu[ignition.msgs.IMU",
            robot_ns + "joint_states@sensor_msgs/msg/JointState[ignition.msgs.Model",
            robot_ns + "lidar/points@sensor_msgs/msg/PointCloud2[ignition.msgs.PointCloudPacked",
            robot_ns + "lidar_vertical/points@sensor_msgs/msg/PointCloud2[ignition.msgs.PointCloudPacked",
            robot_ns + "camera/camera_info@sensor_msgs/msg/CameraInfo[ignition.msgs.CameraInfo"
        ],
        parameters=[
            {
                "qos_overrides./tf_static.publisher.durability": "transient_local",
            }
        ],
        output="screen",
    )

    # Camera image bridge
    image_bridge_rgb = Node(
        package="ros_gz_image",
        executable="image_bridge",
        name="image_bridge" + robot_idx_str,
        arguments=[robot_ns + 'rgb_camera'],
        output="screen"
    )

    bridge = Node(
        package='ros_gz_image',
        executable='image_bridge',
        name="image_bridge" + robot_idx_str,
        arguments=[robot_ns + 'depth_camera'],
        output='screen'
    )
    
    return [
        spawn_robot,
        robot_state_publisher,
        topic_bridge,
        image_bridge_rgb,
        bridge
    ]


def generate_launch_description():
    name_argument = DeclareLaunchArgument(
        "robot_ns",
        default_value="ns12322",
        description="Robot namespace",
    )

    namespace = LaunchConfiguration("robot_ns")

    return LaunchDescription(
        [name_argument, OpaqueFunction(function=spawn_robot, args=[namespace])]
    )
