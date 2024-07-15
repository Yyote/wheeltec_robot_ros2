## Install dependencies

Install ROS2.

```
sudo apt install python3-pip libuvc-dev libopenni2-dev libgflags-dev  ros-$ROS_DISTRO-image-geometry ros-$ROS_DISTRO-camera-info-manager ros-$ROS_DISTRO-image-transport ros-$ROS_DISTRO-image-publisher libgoogle-glog-dev libusb-1.0-0-dev libeigen3-dev nlohmann-json3-dev
```

```
pip3 install openni2 vcstool
```

<!-- ### OpenNI 2 SDK

Download [OpenNI 2 SDK Binaries](https://structure.io/openni/) archive for your system.
Extract it to a directory you like. 

```
cd /path/to/OpenNI
sudo ./install.sh
echo 
``` -->

### HTTPS

```
cd /path/to/wheeltec_robot_ros2
vcs import < https.repos
```

### SSH

```
cd /path/to/wheeltec_robot_ros2
vcs import < ssh.repos
```

### Install udev rules for astra camera
```
cd /your/ros2/ws/src/ros2_astra_camera/astra_camera/scripts
sudo bash install_udev_rules.sh
sudo udevadm control --reload-rules && sudo udevadm trigger
```

### C-SLAM

[Install C-SLAM](https://github.com/MISTLab/Swarm-SLAM) using the instructions. Make it a separate workspace for ease of use.

# Build 

```
colcon build --event-handlers  console_direct+  --cmake-args  -DCMAKE_BUILD_TYPE=Release --packages-select ros2_astra_camera
colcon build
```

