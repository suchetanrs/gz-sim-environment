FROM ubuntu:24.04

#setup
ENV DEBIAN_FRONTEND="noninteractive"

COPY ./shell_scripts/basic_util.sh /root/
RUN cd /root/ && chmod +x * && ./basic_util.sh && rm -rf basic_util.sh
RUN apt-get update && apt-get upgrade -y && apt-get install sudo

COPY shell_scripts/install_ros2_binary.sh /root/
RUN cd /root/ && sudo chmod +x * && ./install_ros2_binary.sh

RUN sudo apt upgrade

RUN sudo apt update
RUN sudo apt install -y python3-rosdep
RUN sudo rosdep init
RUN rosdep update
COPY root_dir/ros2_kilted/ /root/ros2_kilted/
RUN rosdep install --from-paths ~/ros2_kilted/ros2-linux/share --ignore-src -y --skip-keys "cyclonedds fastcdr fastrtps iceoryx_binding_c rmw_connextdds rti-connext-dds-7.3.0 urdfdom_headers fastdds"