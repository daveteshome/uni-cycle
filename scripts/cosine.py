#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String
from std_msgs.msg import Float64
import math

import random

value1 = flag1  = 0

def callback(data):

    global value1 , flag1
    value1 = math.cos(data.data)
    rospy.loginfo("i recive %s", data.data)
    rospy.loginfo("cosine of the vaue i recive is %s", value1)
    flag1 = 1


def cosine():
    
    global value1 ,flag1 
    rospy.init_node('cosine', anonymous=True) 

    pub1 = rospy.Publisher('cosine_output', Float64, queue_size=10)

    sub1 = rospy.Subscriber("cosine_input", Float64, callback)
    

    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():
        if (flag1== 1):
            pub1.publish(value1)
            rospy.loginfo(value1)
            flag1 = 0 
            rate.sleep()
          


    rospy.spin()



if __name__ == '__main__':
    try:
        cosine()
    except rospy.ROSInterruptException:
        pass


