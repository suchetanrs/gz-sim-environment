# A dockerised simulation respository for simulating a vehicle on GZ Sim.
Run ```cd <cloned_repo>```

1. ```git clone https://github.com/suchetanrs/gz-sim-environment -b jazzy && cd gz-sim-environment```
2. ```echo "xhost +" >> ~/.bashrc && source ~/.bashrc``` you can ignore if done already.
3. ```sudo chmod +x install-nvidia-container-toolkit.sh```
4. ```./install-nvidia-container-toolkit.sh```
5. Pull the latest image ```sudo docker pull osrf/ros:jazzy-desktop-full```
6. ```sudo docker build -t gazebo-vehicle-ros2-gpu-harmonic:jazzy .```
7. ```sudo docker compose run vehicle_simulator_gz_sim```
8. ```sudo chmod +x launch_simulation.sh```
9. ```./launch_simulation.sh```
10. This will build the packages in the top-right terminal.
11. After the build is complete you can run what was inputted in the top-left terminal. This will launch gazebo and spawn the robot.
12. The GUI is disabled by default.
13. You should be able to teleop the robot through the teleop window.
14. You can run the default simulation RViz from the bottom-right terminal. As long as you are able to see the lidar pointcloud, the rgb and depth images on RViz, you can safely ignore the texture error messages on the simulation terminal window.

If you would like to install the dependencies of your custom package to use with the simulation, place your custom package in other_ws and build the docker image using step 5 again.

# Important information

The ```ROS_DOMAIN_ID``` is set to 55 in the ```.bashrc```

There are currently two model types. More will be available soon! (Drones, Legged Robots, Multi-Robot Simulations)

You can modify the ```spawn_robot.launch.py``` in the ```vehicle_packages``` to select your desired model.

Edit the `robot_model_type` variable.