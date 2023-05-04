import rclpy
from netifaces import AF_INET, ifaddresses, interfaces
from rclpy.node import Node

from net_msgs.srv import NetworkInfo
from net_msgs.msg import NetworkAddress, NetworkDevice


def get_network_info(ignore_virtual_devices: bool = True):
    """Get network configuration for all devices on the machine.

    uses the system netifaces-class provided as buildin python module.
    """
    netconfig = {}
    for interface in interfaces():
        if ignore_virtual_devices and (
                interface == 'lo'
                or interface.startswith('virbr')
                or interface.startswith('br-')
                or interface.startswith('docker')):
            continue
        ifaddr = ifaddresses(interface)
        if AF_INET in ifaddr:
            netconfig[interface] = ifaddr[AF_INET]
    return netconfig


class NetNode(Node):
    def __init__(self):
        super().__init__('net_node')
        self.get_logger().info('Network service ready')
        self.srv = self.create_service(
            NetworkInfo, 'net_info', self.get_network_info)

    def get_network_info(self, request, response):
        response.devices = []
        net = get_network_info(True)
        for dev_name, dev_addr in net.items():
            addresses = []
            for ip_data in dev_addr:
                addresses.append(NetworkAddress(**ip_data))
            response.devices.append(NetworkDevice(
                name=dev_name,
                addr=addresses
            ))
        return response


def main(args=None):
    rclpy.init(args=args)
    nn = NetNode()
    rclpy.spin(nn)
    nn.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
