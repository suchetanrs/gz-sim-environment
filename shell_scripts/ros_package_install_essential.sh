#!/bin/bash

apt-get update
apt update --fix-missing
apt-get upgrade -y

#rosdep
rosdep init
rosdep update
. /opt/ros/humble/setup.sh
apt-get install python3-rosdep -y
echo '151.101.84.133 raw.githubusercontent.com' | tee -a /etc/hosts
cat /etc/hosts
rosdep init
rosdep update

apt-get install ros-humble-rqt ros-humble-rqt-common-plugins -y
apt-get install ros-humble-rviz2 -y
apt-get install ros-humble-robot-localization -y
sudo apt install ros-humble-ros-gzharmonic -y