from setuptools import setup

package_name = 'net_node'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    requires=['netifaces'],
    zip_safe=True,
    maintainer='Andreas Bresser',
    maintainer_email='andreas.bresser@dfki.de',
    description='ROS 2 Network publication node',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'net_node = net_node.net_node:main'
        ],
    },
)
