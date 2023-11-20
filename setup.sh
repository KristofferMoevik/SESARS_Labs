#!/bin/bash
set -e

#vcs import < src/ros2.repos src
sudo apt-get update
rosdep update
rosdep install --from-paths src --ignore-src -y
# Get gazeebo stuff

sudo apt install ros-humble-turtlesim
export TURTLEBOT3_MODEL=burger
sudo apt install -y xterm

sudo apt install ros-humble-tf-transformations
sudo pip3 install transforms3d

sudo apt install plotjuggler