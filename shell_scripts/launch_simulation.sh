#!/bin/bash

# Check if a session name is provided as an argument, otherwise use 'my_session'
SESSION_NAME=${1:-my_session}

# Start a new tmux session in detached mode with the specified name
tmux new-session -d -s $SESSION_NAME

# In the first (default) pane, run 'echo 3'
tmux send-keys -t $SESSION_NAME "echo 3" C-m

# Split the window horizontally to create a new pane below the current one
tmux split-window -v -t $SESSION_NAME

# In the new pane, run 'echo 4'
tmux send-keys -t $SESSION_NAME "echo 4" C-m

# Attach to the tmux session
tmux attach-session -t $SESSION_NAME
