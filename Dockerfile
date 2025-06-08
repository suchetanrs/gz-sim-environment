FROM nvidia/opengl:1.0-glvnd-devel-ubuntu18.04 AS glvnd
FROM osrf/ros:rolling-desktop-full

#setup
ENV DEBIAN_FRONTEND="noninteractive"

COPY ./shell_scripts/basic_util.sh /root/
RUN cd /root/ && sudo chmod +x * && ./basic_util.sh && rm -rf basic_util.sh
COPY ./shell_scripts/colcon.sh /root/
RUN cd /root/ && sudo chmod +x * && ./colcon.sh && rm -rf colcon.sh
COPY ./shell_scripts/install_gazebo.sh /root/
RUN cd /root/ && sudo chmod +x * && ./install_gazebo.sh && rm -rf install_gazebo.sh
COPY ./shell_scripts/ros_package_install_essential.sh /root
RUN cd /root/ && sudo chmod +x * && ./ros_package_install_essential.sh && rm -rf ros_package_install_essential.sh
RUN apt-get update && apt-get upgrade -y

#GPU related
# Snippet from extension [nvidia]
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglvnd0 \
    libgl1 \
    libglx0 \
    libegl1 \
    libgles2 
COPY --from=glvnd /usr/share/glvnd/egl_vendor.d/10_nvidia.json /usr/share/glvnd/egl_vendor.d/10_nvidia.json
ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:-all}
ENV GZ_VERSION=ionic
RUN apt-get install -y ros-${ROS_DISTRO}-twist-mux ros-${ROS_DISTRO}-pointcloud-to-laserscan
RUN apt-get install -y x11-apps

RUN apt-get install -y ros-${ROS_DISTRO}-bondcpp \
    ros-${ROS_DISTRO}-bond \
    ros-${ROS_DISTRO}-test-msgs \
    libsuitesparse-dev \
    libceres-dev \
    libgraphicsmagick++1-dev \
    graphicsmagick-libmagick-dev-compat \
    libxtensor-dev \
    libomp-dev \
    libbenchmark-dev \
    ros-${ROS_DISTRO}-ompl \
    nlohmann-json3-dev \
    # ros-${ROS_DISTRO}-behaviortree-cpp \
    lcov \
    python3-zmq \
    ros-${ROS_DISTRO}-rmw-cyclonedds-cpp

COPY other_ws/src /root/other_ws/src
RUN cd /root/other_ws && apt-get update && apt-get update --fix-missing && rosdep install --from-paths src --ignore-src -r -y