#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String
from std_msgs.msg import Float64
import math
import random

value1  = flag1  = set_period = 0

def callback(data):
    global value1 , flag1
    value1 = value1 + data.data * set_period
    flag1 = 1

def setperiod(data):
    global set_period
    set_period = data.data

def integrate():
    global value1 , value2 , value3,flag1 ,flag2 , flag3
    rospy.init_node('integrate', anonymous=True)
    pub = rospy.Publisher('integrate_output', Float64, queue_size=10)
    sub = rospy.Subscriber('integrate_input', Float64, callback)
    sub2 = rospy.Subscriber('period_generator', Float64, setperiod)
    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():
        if (flag1== 1):
            pub.publish(value1)
            rospy.loginfo(value1)
            flag1 = 0
            rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        integrate()
    except rospy.ROSInterruptException:
        pass
