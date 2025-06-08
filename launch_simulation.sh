#!/bin/bash

SESSION_NAME="gz_sim_dev_tmux"
tmux new-session -d -s $SESSION_NAME

tmux split-window -h
tmux split-window -v
tmux select-pane -t 0
tmux split-window -v
tmux select-pane -t 1
# tmux split-window -v
# tmux select-pane -t 2
# tmux split-window -v

tmux send-keys -t 0 "cd && source ros2_ws/install/setup.bash && ros2 launch vehicle_bringup unirobot.launch.py "
tmux send-keys -t 1 "cd && source ros2_ws/install/setup.bash && ros2 launch vehicle_bringup octomap.launch.xml"
tmux send-keys -t 2 "cd && cd ros2_ws && colcon build" C-m
tmux send-keys -t 3 "cd && rviz2 -d simulation.rviz"

# Attach to the tmux session
tmux attach-session -t $SESSION_NAME
