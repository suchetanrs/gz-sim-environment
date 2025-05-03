# User input in terminal 1
ros2 run turtlesim turtlesim_node &

sleep 4

echo "==========================ros2 param delete /turtlesim background_b"
ros2 param delete /turtlesim background_b

echo "==========================ros2 param describe /turtlesim background_b"
ros2 param describe /turtlesim background_b

echo "==========================ros2 param dump /turtlesim"
ros2 param dump /turtlesim

echo "==========================ros2 param get /turtlesim background_b"
ros2 param get /turtlesim background_b

echo "==========================ros2 param list /turtlesim"
ros2 param list /turtlesim

echo "==========================ros2 param set /turtlesim background_b 255"
ros2 param set /turtlesim background_b 255