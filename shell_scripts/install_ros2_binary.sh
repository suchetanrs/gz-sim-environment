locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings

sudo apt install -y software-properties-common
sudo add-apt-repository universe

sudo apt update && sudo apt install curl -y
curl -o /tmp/ros2-testing-apt-source.deb https://ftp.osuosl.org/pub/ros/packages.ros.org/ros2-testing/ubuntu/pool/main/r/ros-apt-source/ros2-testing-apt-source_1.0.0~$(. /etc/os-release && echo $VERSION_CODENAME)_all.deb
sudo apt install -y /tmp/ros2-testing-apt-source.deb

sudo apt install -y tar bzip2 wget -y

sudo apt update && sudo apt install -y ros-dev-tools