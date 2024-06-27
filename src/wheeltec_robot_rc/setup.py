from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'wheeltec_robot_rc'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='leev',
    maintainer_email='yyootttaa@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtlebot_teleop_keyboard = wheeltec_robot_rc.turtlebot_teleop_key:main',
            'turtlebot_teleop_keyboard0 = wheeltec_robot_rc.turtlebot_teleop_key_r0:main',
        ],
    },
)