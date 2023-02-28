# ELEC490_CAPSTONE_team5
Indoor Delivery Vehicle


How to run what we have up to this point:

1. Source every terminal with source /opt/ros/foxy.setup.bash
2. Source workspace from root of workspace folder (dev_ws) with source install/setup.bash

Once a terminal has been sourced with the above commands, we can start to use ROS.

1. In the first terminal from dev_ws run: ROS2 launch my_bot launch_robot.launch.py 
 - This will launch the robot in Rviz and beging broadcasting joints and stuff

2. In the second terminal run: Python3 ROS2_Control_Driver.py (located in dev_ws/src/control_bot/control_bot/ros2_control_driver.py)
 - This will start the hardware controller

3. In the third terminal run: ROS2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
 - This will start a terminal to start sending twist commands to move the robot
