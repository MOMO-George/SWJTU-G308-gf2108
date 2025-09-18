#!/usr/bin/env python3
#coding = utf-8

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("pub_py_node")
    rospy.logwarn("python实现消息的发布与接收")

    pub = rospy.Publisher("py",String,queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("py开始发布")
        msg = String()
        msg.data = "2023112108"
        pub.publish(msg)
        rate.sleep()
