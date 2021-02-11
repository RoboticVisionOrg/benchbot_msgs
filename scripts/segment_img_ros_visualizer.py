#!/usr/bin/env python2
import rospy
from benchbot_msgs.msg import SegmentImages
from sensor_msgs.msg import  Image
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--subscribe_topic', '-s', default='isaac_segment',
                     help='topic that we subscribe to in ros', 
                     )
args = parser.parse_args()

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
  rospy.init_node('segment_visualizer', anonymous=True)
  rospy.Subscriber(args.subscribe_topic, SegmentImages, callback)
  rospy.spin()

if __name__ == "__main__":
  listener()

