# BenchBot ROS Messages

[![BenchBot project](https://img.shields.io/badge/collection-BenchBot-%231a2857)](http://benchbot.org)
[![QUT Centre for Robotics Open Source](https://github.com/qcr/qcr.github.io/raw/master/misc/badge.svg)](https://qcr.github.io)
![Primary language](https://img.shields.io/github/languages/top/qcr/benchbot_eval)
[![License](https://img.shields.io/github/license/qcr/benchbot_eval)](./LICENSE.txt)

This repo contains any extra messages used in ROS as part of the BenchBot framework alongside scripts for testing the messages.

# Custom Messages List

- [SegmentImages](#segmentimages)

## SegmentImages

ROS message type containing class and instance segmentation images.

### Message Contents

- `sensor_msgs/Image.msg class_segment_img`
  - `uint8` image where every unique non-zero pixel value corresponds to a specific class
- `sensor_msgs/Image.msg instance_segment_img`
  - `uint16` image where every unique non-zero pixel value corresponds to a specific instance
  - numbering convention of pixel values is CCIII where CC is the class id (1 up to 65) and III is the instance id within the current environment (1 up to 999)
- `string[] class_names`
  - name of each class in the given image as a string
- `uint16[] class_ids`
  - corresponding class id for each entry in `class_names`
  - note that `class_ids` must be non-zero as zero is allocated to background pixels.

### Test Scripts

#### `segment_img_ros_visualizer.py`

This script simply publishes the individual image components of the SegmentImages message to ros to be visualized using `rqt_image_view` or `rviz`.

**Arguments:**

- `--subscribe_topic`, `-s` - the ROS topic to subscribe to

#### `segment_img_save_img_test.py`

This script saves every mask for every class segmentation image (every individual class) and every instance segmentation image (every individual instance) as its own image.

**THIS USES UP STORAGE SPACE VERY QUICKLY AND SHOULD BE ONLY USED FOR QUICK TESTS**

**Arguments:**

- `--subscribe_topic`, `-s` - the ROS topic to subscribe to
- `--img_folder`, `-i` - the location where images will be saved

