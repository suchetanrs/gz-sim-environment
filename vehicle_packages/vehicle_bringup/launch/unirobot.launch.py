import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Setup project paths
    pkg_ros_gz_sim = get_package_share_directory("ros_gz_sim")
    pkg_project_gazebo = get_package_share_directory("vehicle_bringup")
    pkg_project_worlds = get_package_share_directory("gz_sim_worlds")

    # Setup to launch the simulator and Gazebo world
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, "launch", "gz_sim.launch.py")
        ),
        launch_arguments={"gz_version": "8",
                          "gz_args": "--headless-rendering -r -s playpen_featureless_diag.sdf"}.items(),
    )
    # clearpath_playpen.sdf
    # pittsburgh_mine.sdf
    # inspection.sdf
    # marsyard2022.sdf
    # playpen_featureless.sdf
    # indoor.sdf
    
    # if you wish to use gazebo without the GUI (increases RTF) use the arguments,
    # --headless-rendering -r -s clearpath_playpen.sdf

    # Bridge ROS topics and Gazebo messages for establishing communication
    topic_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        name="clock_bridge",
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock",
            "tf@tf2_msgs/msg/TFMessage[ignition.msgs.Pose_V",
        ],
        parameters=[
            {
                "qos_overrides./tf_static.publisher.durability": "transient_local",
            }
        ],
        output="screen",
    )

    spawn_robots = [
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_project_gazebo, "launch", "vehicle_gz.launch.py")
            ),
            launch_arguments={"robot_ns": f"robot_{i}/"}.items(),
        )
        for i in range(0, 1)
    ]

    return LaunchDescription(
        [
            gz_sim,
            topic_bridge,
        ] + spawn_robots
    )
