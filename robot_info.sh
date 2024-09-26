export ROBOT_NAME=r                       # Required!
export ROBOT_ID=1                         # Required!
export ROBOT_CAMERA_CAPABILITIES=astra_s  # Required!
export ROS_DOMAIN_ID=207
export ROBOT_TYPE=omnid                 # Required! [tracked, ackerman, omni]

echo Robot name = ${ROBOT_NAME}
echo Robot id = ${ROBOT_ID}
echo ROS DOMAIN ID = ${ROS_DOMAIN_ID}
echo Robot info sourced.
