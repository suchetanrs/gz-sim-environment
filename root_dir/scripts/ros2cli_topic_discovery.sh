echo "========================== starting ros2 launch demo_nodes_cpp talker_listener_launch.py"
ros2 launch demo_nodes_cpp talker_listener_launch.py &

sleep 1
echo "========================== topic list below"
ros2 topic list

sleep 4
echo "========================== killing ros2 launch demo_nodes_cpp talker_listener_launch.py"
kill -SIGINT $(pidof talker)
while pidof talker >/dev/null; do sleep 0.5; done

kill -SIGINT $(pidof listener)
while pidof listener >/dev/null; do sleep 0.5; done

sleep 20

echo "========================== topic list after kill"
ros2 topic list