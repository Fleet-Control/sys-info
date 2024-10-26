# System Node
ROS 2 System information node.

Allows you to get information on your ROS 2 robot via ROS 2 itself.

## Installation

Clone the repository in your ros-workspace and build using colcon:
```bash
cd ~/ros_ws/src
git clone https://github.com/Fleet-Control/net-node.git
colcon build
```
after successful installation re-source your ROS workspace.

## Usage

Start the "NetNode" node
```bash
ros2 run sys_info sys_info
```

Then you can get network information about the host system of your ROS2 node,
for example:

```bash
ros2 service call /net_info sys_msgs/srv/NetworkInfo
```
