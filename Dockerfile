FROM nvidia/opengl:1.0-glvnd-devel-ubuntu18.04 as glvnd
FROM osrf/ros:humble-desktop-full-jammy

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
ENV GZ_VERSION harmonic
# COPY ./root_dir/ros2_ws/ /root/ros2_ws/
# RUN cd /root/ros2_ws/ && rosdep install --from-paths src --ignore-src -r -y