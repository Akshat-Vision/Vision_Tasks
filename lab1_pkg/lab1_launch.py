#!/usr/bin/env python3

import rospy
import roslaunch
from std_msgs.msg import String

def launch_nodes():
    rospy.init_node('lab1_launch', anonymous=True)

    # Set parameters for the talker node
    rospy.set_param('/talker_node/v', 1.5)
    rospy.set_param('/talker_node/d', 0.3)

    # Define the launch configuration for the talker node
    talker_node = roslaunch.core.Node(
        package='lab1_pkg',
        node_type='talker.py',
        name='talker_node',
        output='screen'
    )

    # Define the launch configuration for the relay node
    relay_node = roslaunch.core.Node(
        package='lab1_pkg',
        node_type='relay.py',
        name='relay_node',
        output='screen'
    )

    # Create a launch object and add nodes to it
    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()

    # Add nodes to the launch object
    launch.launch(talker_node)
    launch.launch(relay_node)

if __name__ == '__main__':
    try:
        launch_nodes()
    except rospy.ROSInterruptException:
        pass

