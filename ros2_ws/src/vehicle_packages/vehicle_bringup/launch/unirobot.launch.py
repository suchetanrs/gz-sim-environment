import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch.conditions import IfCondition, UnlessCondition


def generate_launch_description():
    # Setup project paths
    pkg_ros_gz_sim = get_package_share_directory("ros_gz_sim")
    pkg_project_gazebo = get_package_share_directory("vehicle_bringup")
    pkg_project_worlds = get_package_share_directory("gz_sim_worlds")

    world_arg = DeclareLaunchArgument(
        name="world",
        default_value="marsyard2020_walls.sdf",
        description="Name of the Gazebo world file (SDF) in gz_sim_worlds/worlds/"
    )
    world_file = LaunchConfiguration("world")

    # Setup to launch the simulator and Gazebo world
    headless_arg = DeclareLaunchArgument(
        name="headless",
        default_value="true",
        description="Run Gazebo in headless (no GUI) mode"
    )
    headless = LaunchConfiguration("headless")

    base_launch_args = {
        "gz_version": "8",
        "gz_args": ["--headless-rendering -r ", world_file],
    }

    # extend for headless
    headless_launch_args = {
        **base_launch_args,
        "gz_args": [" -s ", *base_launch_args["gz_args"]],
    }
    
    gui_launch_args = base_launch_args

    gz_sim_headless = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, "launch", "gz_sim.launch.py")
        ),
        launch_arguments=headless_launch_args.items(),
        condition=IfCondition(headless),
    )
    
    gz_sim_gui = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, "launch", "gz_sim.launch.py")
        ),
        launch_arguments=gui_launch_args.items(),
        condition=UnlessCondition(headless),
    )
    # clearpath_playpen.sdf
    # pittsburgh_mine.sdf
    # inspection.sdf
    # marsyard2022.sdf
    # playpen_featureless.sdf
    # playpen_featureless_diag.sdf
    # indoor.sdf
    
    # if you wish to use gazebo without the GUI (increases RTF) use the arguments,
    # --headless-rendering -r -s clearpath_playpen.sdf

    # Bridge ROS topics and Gazebo messages for establishing communication
    topic_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        name="clock_bridge",
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock",
            # "tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V",
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
            # launch_arguments={"robot_ns": f"robot_{i}/"}.items(),
            launch_arguments={"robot_ns": ""}.items(),
        )
        for i in range(0, 1)
    ]

    return LaunchDescription(
        [
            world_arg,
            headless_arg,
            gz_sim_gui,
            gz_sim_headless,
            topic_bridge,
        ] + spawn_robots
    )
