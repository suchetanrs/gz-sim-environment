#!/bin/bash

export DEBIAN_FRONTEND="noninteractive"
apt-get update
apt-get upgrade
apt-get update --fix-missing
apt-get install -y sudo git-all lsb-release curl nano tmux vim ranger xterm nautilus 