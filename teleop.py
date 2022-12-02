#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

x = 0.0
z = 0.0

def callback(data):
    global x, z
    x = data.axes[1]
    z = data.axes[0]

def talker():
    global x, z
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(20) # 10hz
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 5*x
        twist.angular.z = 2*z
        rospy.loginfo(twist)
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    rospy.Subscriber("joy", Joy, callback)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
