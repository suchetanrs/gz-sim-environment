cd ~/scripts
echo "============================================System info======================================================"
echo "architecure: $(uname -m)"
echo "middleware: $(ros2 doctor --report | grep 'middleware')"


echo "============================================Running ros2 help======================================================"

./ros2_help.sh

echo "============================================Running node discovery==========================================="

./ros2cli_node_discovery.sh

echo "============================================Running topic discovery==========================================="

./ros2cli_topic_discovery.sh

echo "============================================Running service discovery==========================================="

./ros2cli_service_discovery.sh

echo "============================================Running param completion==========================================="

./ros2cli_param_discovery.sh