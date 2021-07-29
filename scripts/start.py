#!/usr/bin/env python3
# -- coding: utf-8 --

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

pub = None

def laser_readings(msg):
    parts = {
      'right': min(min(msg.ranges[0:59]),1),
      'straight': min(min(msg.ranges[60:119]),1),
      'left': min(min(msg.ranges[120:179]),1), 
    }
    rospy.loginfo(parts)
    logic(parts)

def logic(parts):
  linear_speed_x = 0
  angular_speed_z = 0
  msg = Twist()


  if parts['right'] > 0.7 and parts['straight'] < 0.7 and parts['left'] < 0.7 :
      linear_speed_x = 0.5
      angular_speed_z = -0.5

  elif parts['right'] > 0.7 and parts['straight'] > 0.7 and parts['left'] < 0.7 :
      linear_speed_x = 0.5
      angular_speed_z = -0.5

  elif parts['right'] > 0.7 and parts['straight'] > 0.7 and parts['left'] > 0.7 :
      linear_speed_x = 0.5
      angular_speed_z = 0

  elif parts['right'] < 0.7 and parts['straight'] > 0.7 and parts['left'] < 0.7 :
      linear_speed_x = 0.5
      angular_speed_z = 0
   
  elif parts['right'] < 0.7 and parts['straight'] > 0.7 and parts['left'] > 0.7 :
      linear_speed_x = 0.5
      angular_speed_z = 0.5

  elif parts['right'] > 0.7 and parts['straight'] < 0.7 and parts['left'] > 0.7 :
      linear_speed_x = 0.5
      angular_speed_z = 0.5

  elif parts['right'] < 0.7 and parts['straight'] < 0.7 and parts['left'] > 0.7 :
      linear_speed_x = 0.5
      angular_speed_z = 0.5

  elif parts['right'] < 0.7 and parts['straight'] < 0.7 and parts['left'] < 0.7 :
      linear_speed_x = 0
      angular_speed_z = -0.5

  else:
      rospy.loginfo(parts)

  msg.linear.x = linear_speed_x
  msg.angular.z = angular_speed_z
  pub.publish(msg)

def main():
    global pub
    rospy.init_node('obs_avoid')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    sub = rospy.Subscriber("/m2wr/laser/scan",LaserScan,laser_readings)

    rospy.spin()

if __name__ == '__main__':
  main()
