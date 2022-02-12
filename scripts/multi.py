#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int64
from std_msgs.msg import String
from std_msgs.msg import Float64
import random

value1 = value2 = flag1 = flag2 = 0

def callback(data):
    global value1 , flag1
    value1 = data.data 
    rospy.loginfo("I heard %s", data.data)
    flag1 = 1

def callback2(data):
    global value2 , flag2
    value2 = data.data 
    rospy.loginfo( "I heard%s", data.data)
    flag2 =1


def multi():
    
    global value1 , value2  ,flag1 ,flag2 

    rospy.init_node('multi', anonymous=True) 

    pub1 = rospy.Publisher('multi_output', Float64, queue_size=10)
    sub1 = rospy.Subscriber('multi_input_1', Float64, callback)
    sub2 = rospy.Subscriber('multi_input_2', Float64, callback2)

    rate = rospy.Rate(100) # 10hz
    while not rospy.is_shutdown():
        if (flag1 and flag2 ):
            pub1.publish(value1 * value2)
            flag1 = 0
            flag2 = 0 
            rospy.loginfo(value1 * value2)
            rate.sleep()

    rospy.spin()



if __name__ == '__main__':
    try:
        multi()
    except rospy.ROSInterruptException:
        pass
