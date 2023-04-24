#!/usr/bin/env python3
import rospy
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
from turtlesim.srv import Kill
from std_msgs.msg import String
import sys
l_name = []
l_point = []
delete_list=[]
game_points = 0
def points(msg):

    global l_name
    global l_point
    l = msg.data
    l = l.split(' ')
    l_name.append(l[2])
    l_point.append(l[:2])


def killturtle(n):
    global game_points,delete_list
    if n not in delete_list:
        kill_turt = rospy.ServiceProxy("kill", Kill)
        game_points = game_points + 1
        response1 = kill_turt(n)
        delete_list.append(n)
    else:
        pass

def pose_val(pose:Pose):
    int_x = round(pose.x)
    int_y = round(pose.y)
    fin_x = str(round(pose.x))+".0"
    fin_y = str(round(pose.y))+".0"

    if ([fin_x, fin_y]) in l_point:
        val = l_point.index([fin_x,fin_y])

        killturtle(l_name[val])

    
if __name__ == '__main__':
    rospy.init_node("get_point_node") 
    l_point = []
    l_name = [] 
    sub1 = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_val)
    sub = rospy.Subscriber("points", String, callback=points)
    rospy.spin()
    if rospy.is_shutdown():
        rospy.loginfo("your total points : "+str(game_points))


