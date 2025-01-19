#SUCHETAN
echo 'export XDG_RUNTIME_DIR=/tmp/runtime-root' >>/root/.bashrc

echo "alias ranger='ranger --choosedir=/root/.rangerdir; LASTDIR=\`cat /root/.rangerdir\`; cd ""\$LASTDIR""'" >> /root/.bashrc
echo "alias cdros='cd /root/ros2_ws/'" >> /root/.bashrc
echo "alias sws='source /root/ros2_ws/install/setup.bash && source /root/slam_ws/install/setup.bash && source /root/dev_ws/install/setup.bash'" >> /root/.bashrc
echo "alias sros='source /opt/ros/$ROS_DISTRO/setup.bash'" >> /root/.bashrc

#ROS!
echo 'source /opt/ros/$ROS_DISTRO/setup.bash' >> /root/.bashrc
echo "export TURTLEBOT3_MODEL=waffle" >> /root/.bashrc

echo "export GAZEBO_MODEL_PATH=\$GAZEBO_MODEL_PATH:/root/ros2_ws/src/leo_rover/leo_desktop-ros2/leo_gazebo_worlds/models/" >> /root/.bashrc

#PERMISSIONS
sudo -E chmod -R a+rw /dev