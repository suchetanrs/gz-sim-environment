echo "==========================starting turtlesim"

ros2 run turtlesim turtlesim_node &
sleep 2

echo "==========================param list below"
ros2 param list

echo "==========================killing turtlesim"
kill -SIGINT $(pidof turtlesim_node)
while pidof turtlesim_node >/dev/null; do sleep 0.5; done

sleep 20

echo "==========================param list after kill"
ros2 param list
