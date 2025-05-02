echo "========================== starting add_two_ints_server"
ros2 run demo_nodes_cpp add_two_ints_server &

sleep 1
echo "========================== service list below"
ros2 service list

echo "========================== killing add_two_ints_server"
kill -SIGINT $(pidof add_two_ints_server)
while pidof add_two_ints_server >/dev/null; do sleep 0.5; done

sleep 20

echo "========================== service list after kill"
ros2 service list
