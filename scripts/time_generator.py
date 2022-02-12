#!/usr/bin/env python
# license removed for brevity
import rospy
from beginner_tutorials.msg import Num
from std_msgs.msg import String
from std_msgs.msg import Int64
from std_msgs.msg import Float64
import random
value = 0
frq = 60
set_period = 1/frq

def time_generator():
    global value , set_period , frq
    rospy.init_node('time_generator', anonymous=True)

    pub = rospy.Publisher('time_generator_output', Float64, queue_size=10)
    pub2 = rospy.Publisher('period_generator', Float64, queue_size=10)
    rate = rospy.Rate(frq) # 0.25 sec

    while not rospy.is_shutdown():

        rospy.loginfo(value)
        pub2.publish(set_period)
        pub.publish(value)
        value = value + set_period
        rate.sleep()

if __name__ == '__main__':
    try:
        time_generator()
    except rospy.ROSInterruptException:
        pass
