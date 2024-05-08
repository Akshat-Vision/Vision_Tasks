#!/usr/bin/env python3

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

def callback(msg):
    msg.drive.speed *= 3
    msg.drive.steering_angle *= 3
    pub.publish(msg)

rospy.init_node('relay')
sub = rospy.Subscriber('drive', AckermannDriveStamped, callback)
pub = rospy.Publisher('drive_relay', AckermannDriveStamped, queue_size=10)

rospy.spin()
