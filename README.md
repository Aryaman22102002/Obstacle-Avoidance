# Obstacle-Avoidance

## Prerequisites
•	ROS </br>
•	Gazebo

## File Structure 
    ├── Launch                            # Launch files of the robot and some of the worlds
        ├── spawn.launch         
        ├── world1.launch            
        ├── world2.launch         
        ├── world3.launch
        ├── world4.launch
    ├── scripts                           # The obstacle avoidance algorithm
        ├── start.py                
    ├── urdf                              # The file which contains the details about the robot and the sensor
        ├── m2wr.xacro 
    ├── worlds                            # The world files which contain information about different worlds 
        ├── assignment_world.world        
        ├── turtlebot3_stage_1.world            
        ├── turtlebot3_stage_2.world          
        ├── turtlebot3_stage_3.world
        ├── turtlebot3_stage_4.world
        ├── turtlebot3_world.world
        ├── world01.world          
        ├── world02.world
        ├── world03.world
        ├── world04.world
    ├── CMakeLists.txt
    ├── LICENSE
    ├── README.md
    ├── package.xml
    
## Steps to get started
1. Clone this repository in your src.
2. Run <code> catkin_make </code>.
3. Run the command <code> roslaunch obstacle_avoidance spawn.launch </code> to launch gazebo, the bot and your world.
4. You can change the world by changing the name of the world file name in the spawn.launch file.
5. You can also change the position where the bot will spawn in the spawn.launch file.
6. Now open a second terminal and run the following command</br> <code>chmod +x ~/catkin_ws/src/obstacle_avoidance/scripts/start.py</code> or go into your scripts folder and then run the command</br><code>chmod +x start.py</code> .
8. run the following command <code>rosrun obstacle_avoidance start.py</code> to start your obstacle avoidance algorithm.

## Video
https://user-images.githubusercontent.com/82901720/127613259-70f9b875-37d4-4038-b433-d08cfe0e3c6e.mp4

## Contributor
•	[Aryaman Shardul](https://github.com/Aryaman22102002)

## Acknowledgements and Resources
•	[SRA VJTI](https://www.sravjti.in/) </br>
•	Special thanks to [Gautam Agrawal](https://github.com/gautam-dev-maker) and [Saad Hashmi](https://github.com/hashmis79) </br>
•	https://github.com/ROBOTIS-GIT/turtlebot3_simulations</br>
• https://github.com/SravanChittupalli/Path-Planning-Algorithms-Part2

## License
The [License](https://github.com/Aryaman22102002/Obstacle-Avoidance/blob/main/LICENSE) used for this project.



