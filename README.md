# A dockerised simulation respository for simulating a vehicle on GZ Sim.
Run ```cd <cloned_repo>```

1. ```sudo docker build -t gazebo-vehicle-ros2-gpu-harmonic:humble .```
2. ```sudo docker compose run vehicle_simulator_gz_sim```
3. Once inside the container run ```cd ros2_ws/ && colcon build```
4. ```source ~/.bashrc```
5. To setup gazebo for the first time, run ```ros2 launch vehicle_bringup unirobot.launch.py ```. This can quite a bit of time (Patience is key :p). Once the Gazebo GUI is open and you can see, move around and interact with the world, you can close this launch file. Gazebo is set for future use.
6. To launch the robot simulation after running (5), run ```ros2 launch vehicle_bringup unirobot.launch.py```
7. You should be able to teleop the robot through the teleop window in gazebo.

# Important information
The namespace of the robot is currently set to ```robot_0```.
The ```ROS_DOMAIN_ID``` is set to 55 in the ```.bashrc```
There are currently two model types. More will be available soon! (Drones, Legged Robots, Multi-Robot Simulations)
You can modify the ```spawn_robot.launch.py``` in the ```vehicle_packages``` to select your desired model.
You can choose from ```model``` and ```model_with_2_lidars```

![MarsYard](media/marsyard.png)
![Clearpath](media/playpen.png)
![Inspection](media/inspection.png)