# Net Node
ROS 2 Network information and configuration node.

Allows you to configure your ROS 2 robot network configuration via ROS itself.

## Usage

Start the "NetNode" node
```bash
ros2 run net_node net_node
```

Then you can get network information about the host system of your ROS2 node,
for example:

```bash
ros2 service call /net_info net_msgs/srv/NetworkInfo
```