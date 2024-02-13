# Turtlesim visualiser in rviz

Enter the followeing commands to visualise an arrow in rviz. The commands are sent via the turtlesim keyboard teleop node

```
cd ¬/catkin_ws/src

git clone https://github.com/venkateshsripada/tutorial_mini.git

cd ~/catkin_ws

catkin_make

source devel/setup.bash

chmod +x ~/catkin_ws/src/tutorial_mini/tutorials/src/tutorial.py 
```

Now run the following in different terminals

Terminal1
```
rosrun turtlesim turtsim_node
```

Terminal 2
```
rosrun turtlesim turtle_teleop_key
```

Terminal 3
```
cd ~/catkin_ws/src

rosrun tutorials tutorial.py
```

Terminal 4
```
rosrun rviz rviz
```

Once rviz is launched. On the top left, press, "File -> open config -> turtle_rviz.rviz" 

To move the arrow in rviz, go to "Terminal 2" where you launched the turtle_teleop_key. Press on the arrow keys on your keyboard
