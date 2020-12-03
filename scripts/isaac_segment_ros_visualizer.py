#!/usr/bin/env python2
import rospy
from benchbot_msgs.msg import isaac_segment_img
from sensor_msgs.msg import  Image

# Visualizer here simply takes the complete custom ros msg
# splits it into its component parts and publishes them back to ROS
pub_class = rospy.Publisher('class_segment_img', Image, queue_size=10)
pub_inst = rospy.Publisher('instance_segment_img', Image, queue_size=10)

def callback(data):
  # Do I need something to sync the timestamps of these images or does
  # it stay the same from the original message?
  pub_class.publish(data.class_segment_img)
  pub_inst.publish(data.instance_segment_img)

def visualizer(data):
  rate = rospy.Rate(10)

def listener():
  rospy.init_node('isaac_segment_visualizer', anonymous=True)
  rospy.Subscriber("isaac_segment", isaac_segment_img, callback)
  rospy.spin()

if __name__ == "__main__":
    listener()

