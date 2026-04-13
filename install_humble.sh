#!/bin/bash
# Script to install ROS 2 Humble on Ubuntu 22.04 Jammy Jellyfish

set -e 

echo "--- 1. Configuring Locales ---"
sudo apt update && sudo apt install locales -y
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

echo "--- 2. Setting up Software Properties ---"
sudo apt install software-properties-common -y
sudo add-apt-repository universe -y

echo "--- 3. Installing Curl and Adding ROS 2 Key ---"
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "--- 4. Configuring ROS 2 Sources ---"
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

echo "--- 5. Updating and Upgrading System ---"
sudo apt update
sudo apt upgrade -y

echo "--- 6. Installing ROS 2 Humble Desktop ---"
sudo apt install ros-humble-desktop -y

echo "--- 7. Installing Build Tools (Colcon & Rosdep) ---"
sudo apt install python3-colcon-common-extensions python3-rosdep python3-argcomplete -y

echo "--- 8. Initializing Rosdep ---"
if [ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then
    sudo rosdep init
fi
rosdep update

echo "--- 9. Setting up Environment ---"
if ! grep -q "source /opt/ros/humble/setup.bash" ~/.bashrc; then
  echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
fi

echo "--- DONE! ---"
echo "Please restart your terminal or run: source ~/.bashrc"
