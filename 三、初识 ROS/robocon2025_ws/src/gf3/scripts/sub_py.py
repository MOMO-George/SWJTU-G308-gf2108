#!/usr/bin/env python3
#coding = utf-8

import rospy
from std_msgs.msg import String

def sub_callback(msg):
    rospy.loginfo(msg.data)

if __name__ == "__main__":
    rospy.init_node("sub_py_node")

    sub = rospy.Subscriber("py",String,sub_callback,queue_size=10)

    rospy.spin()
