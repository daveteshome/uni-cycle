#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String
from std_msgs.msg import Float64
import math
import random

value1 ,flag1 = 0

def callback(data):
    global value1 , flag1
    value1 = data.data*0.5
    flag1 = 1

def constant():
    global value1 , value2 ,flag1 ,flag2
    rospy.init_node('constant', anonymous=True)
    pub = rospy.Publisher('constant_output', Float64, queue_size=10)
    sub = rospy.Subscriber("constant_input", Float64, callback)

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
        constant()
    except rospy.ROSInterruptException:
        pass
