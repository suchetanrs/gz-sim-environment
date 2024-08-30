#!/bin/bash

export DEBIAN_FRONTEND="noninteractive"
apt-get update
apt-get upgrade
apt-get update --fix-missing
apt-get install git-all -y
apt-get update --fix-missing
apt-get install lsb-release -y
apt-get install curl -y
apt-get install nano -y
apt-get install tmux -y
apt-get install mlocate -y
apt-get install vim -y
apt-get install ranger -y
apt-get install xterm -y
apt-get install nautilus -y