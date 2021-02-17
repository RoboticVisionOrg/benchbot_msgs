#!/usr/bin/env python2
import rospy
from benchbot_msgs.msg import SegmentImages
from cv_bridge import CvBridge
import os
import cv2
import numpy as np


parser = ArgumentParser()
parser.add_argument('--subscribe_topic', '-s', default='isaac_segment',
                     help='topic that we subscribe to in ros', 
                     )
parser.add_argument('--img_folder', '-i', default='./',
                    help='location where images will be saved')
args = parser.parse_args()
root_folder = args.img_folder

count = 0
# This just saves each individual class and instance in an image as its own image
# Used to confirm everything is working correctly.
# USES A LOT OF MEMORY QUICKLY!!! DO NOT RUN FOR LONG

def callback(data):
  global count
  # create a folder where the sub-images for this data will be stored
  subfolder = os.path.join(root_folder, "{:06d}".format(count))
  if not os.path.isdir(subfolder):
    os.makedirs(os.path.join(subfolder, "class"))
    os.makedirs(os.path.join(subfolder, "instance"))
  
  # Get the class image as a numpy array (cv2)
  bridge = CvBridge()
  class_img = bridge.imgmsg_to_cv2(data.class_segment_img, "8UC1")

  # Get the class names and ids
  class_ids = np.array(data.class_ids, dtype=np.uint8)
  class_names = np.array(data.class_names)

  # save the class image for each individual class
  for class_id in np.unique(class_img):
    # Ignore the "not labelled" pixels
    if class_id == 0:
      continue

    # find the class name to use in image name
    class_name = class_names[np.where(class_ids == class_id)[0]][0]
    img_name = os.path.join(subfolder, "class", 
                            "{0:03d}_{1}.png".format(class_id, class_name))
    cv2.imwrite(img_name, (class_img == class_id)*255)
  
  # Get the instance image
  instance_img = bridge.imgmsg_to_cv2(data.instance_segment_img, "16UC1")
  # save the instance image for each individual instance
  for instance_id in np.unique(instance_img):
    # skip the "unlabelled pixels" with value zero
    if instance_id == 0:
      continue
    # determine the class of the instance in the image using the class segment
    bool_inst_img = instance_img == instance_id
    masked_class_img = class_img * bool_inst_img
    # should only have the current class object in this mask
    class_name = class_names[np.where(class_ids == np.max(masked_class_img))[0]][0]
    img_name = os.path.join(subfolder, "instance", "{0:06d}_{1}.png".format(instance_id, class_name))
    cv2.imwrite(img_name, bool_inst_img*255)
  count += 1


def listener():
  rospy.init_node('SegmentImages_tester', anonymous=True)
  rospy.Subscriber(args.subscribe_topic, SegmentImages, callback)
  rospy.spin()

if __name__ == "__main__":
  listener()

