#!/usr/bin/env python3

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

def talker():
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10Hz
    pub = rospy.Publisher('drive', AckermannDriveStamped, queue_size=10)

    while not rospy.is_shutdown():
        v = rospy.get_param('~v', 0.0)  # Default value is 0.0
        d = rospy.get_param('~d', 0.0)  # Default value is 0.0
        msg = AckermannDriveStamped()
        msg.drive.speed = v
        msg.drive.steering_angle = d
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

