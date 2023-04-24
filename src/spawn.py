#!/usr/bin/env python3
import rospy
from turtlesim.srv import Spawn
from turtlesim.srv import SetPen
import time
import random
import math
from std_msgs.msg import String

def spawn(x,y,theta,name):

    spawns = rospy.ServiceProxy("spawn",Spawn)
    response = spawns(x,y,theta,name)

    msg = str(x)+' '+str(y)+' '+str(name)
    pub.publish(msg)  


    time.sleep(3)

def set_pen(r,g,b,width,off):

    set = rospy.ServiceProxy("/turtle1/set_pen",SetPen)
    res = set(r,g,b,width,off)



l = []
i = 0
if __name__ == '__main__':
    rospy.init_node("catcher_node")
    rospy.wait_for_service("/spawn")   
    pub = rospy.Publisher("points", String, queue_size=10)
    rate = rospy.Rate(10)
    set_pen(0,0,0,2,1)

    time.sleep(1)
    while True:

        i = i+1
        x = float(random.randint(1,9))
        y = float(random.randint(1,9))
        t = float(random.randint(0,9))/6.28
        name = str("turtle30")+str(i)
        spawn(x,y,t,name)
