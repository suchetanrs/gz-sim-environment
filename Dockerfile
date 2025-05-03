FROM ubuntu:24.04

#setup
ENV DEBIAN_FRONTEND="noninteractive"

COPY ./shell_scripts/basic_util.sh /root/
RUN cd /root/ && chmod +x * && ./basic_util.sh && rm -rf basic_util.sh
RUN apt-get update && apt-get upgrade -y && apt-get install sudo

COPY shell_scripts/install_ros2_deb.sh /root/
RUN cd /root/ && sudo chmod +x * && ./install_ros2_deb.sh

RUN sudo apt upgrade

RUN sudo apt update
RUN sudo apt install -y python3-rosdep
RUN sudo rosdep init
RUN rosdep update