# User input in terminal 1
echo "==========================uname -m"
uname -m

echo "==========================middleware"
ros2 doctor --report | grep "middleware"

echo "==========================ros2 doctor -r"
ros2 doctor -r

# User input in terminal 1
echo "==========================ros2 doctor -rf"
ros2 doctor -rf

# User input in terminal 1
echo "==========================ros2 doctor -iw"
ros2 doctor -iw

# User input in terminal 1
echo "==========================ros2 hello"
ros2 doctor hello
