import os


def ros_id():
    if 'ROS_DOMAIN_ID' in os.environ:
        return os.environ['ROS_DOMAIN_ID']
    # All ROS 2 nodes use domain ID 0 by default
    return '0'
