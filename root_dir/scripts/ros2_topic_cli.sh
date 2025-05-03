echo "==================ros2 launch dummy_robot_bringup dummy_robot_bringup_launch.py"
ros2 launch dummy_robot_bringup dummy_robot_bringup_launch.py &

sleep 5

echo "==================ros2 topic bw /joint_states"
timeout 5s ros2 topic bw /joint_states

echo "==================ros2 topic delay /joint_states"
timeout 5s ros2 topic delay /joint_states

echo "==================ros2 topic echo /joint_states"
timeout 1s ros2 topic echo /joint_states

echo "==================ros2 topic find sensor_msgs/msg/JointState"
timeout 5s ros2 topic find sensor_msgs/msg/JointState

echo "==================ros2 topic hz /joint_states"
timeout 5s ros2 topic hz /joint_states

echo "==================ros2 topic info /joint_states"
timeout 5s ros2 topic info /joint_states

echo "==================ros2 topic list"
timeout 5s ros2 topic list

echo "==================ros2 topic type /joint_states"
timeout 5s ros2 topic type /joint_states

ros2 run demo_nodes_cpp listener &

ros2 topic pub /chatter std_msgs/msg/String "{data: 'hi'}"