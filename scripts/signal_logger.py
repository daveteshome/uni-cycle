#!/usr/bin/env python
# license removed for brevity
import rospy
import matplotlib.pyplot as plt
from std_msgs.msg import Int64
from std_msgs.msg import String
from std_msgs.msg import Float64
import math
import random

value1 = value2 = flag1 = flag2 = 0
x = []
y = []

def callback(data):
    global value1 , flag1
    value1 = data.data
    flag1 = 1
    my_append()

def callback2(data):
    global value2 , flag2
    value2 = data.data
    flag2 = 1
    my_append()

def my_append():
    global flag1 , flag2
    if (flag1 and flag2 ):
        x.append(value1)
        y.append(value2)
        flag1 = 0
        flag2 = 0
        rospy.loginfo("The valve of %f x, %f y  ", value1 ,value2 )

def signal_logger():
    global value1 , value2 , flag1 ,flag2
    rospy.init_node('signal_logger', anonymous=True) 
    sub = rospy.Subscriber('signal_logger_input_1', Float64, callback)
    sub2 = rospy.Subscriber('signal_logger_input_2', Float64, callback2)
    rate = rospy.Rate(100) # 10hz
    rospy.spin()

if __name__ == '__main__':
    try:
        signal_logger()
        # Add a legend
        plt.legend()
        if rospy.is_shutdown():
            #plot
            plt.plot(x, y, label='position Of Uni Cycle Robot Model')
            plt.show()
    except rospy.ROSInterruptException:
        pass
