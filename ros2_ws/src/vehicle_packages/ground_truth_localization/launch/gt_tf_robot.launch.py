#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.actions import IncludeLaunchDescription, OpaqueFunction
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, FindExecutable, TextSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

#---------------------------------------------

    #Essential_paths
    name_argument = DeclareLaunchArgument(
        "robot_ns",
        default_value="robot_0",
        description="Robot namespace",
    )

    namespace = LaunchConfiguration("robot_ns")
    
#---------------------------------------------

    def all_nodes_launch(context):
        params_file = LaunchConfiguration('params_file')

        publish_tf = Node(
            package='ground_truth_localization',
            executable='publish_tf',
            namespace=namespace,
            output='screen')
        
        return [publish_tf]

    opaque_function = OpaqueFunction(function=all_nodes_launch)
#---------------------------------------------

    return LaunchDescription([
        name_argument,
        opaque_function
    ])