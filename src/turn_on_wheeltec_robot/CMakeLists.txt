cmake_minimum_required(VERSION 3.8)
project(turn_on_wheeltec_robot)

cmake_policy(SET CMP0057 NEW)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# find_package(rclpy REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
# find_package(serial REQUIRED)
# find_package(roslib REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)


set(COLCON_VARS ament_cmake geometry_msgs rclcpp tf2_ros tf2_geometry_msgs nav_msgs nav_msgs sensor_msgs std_msgs tf2) # roslib

# find_package(rospy REQUIRED)

add_compile_options(-g -std=c++17)    #-g -> core dumped

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# add_library( ${serial_SRCS})


if(APPLE)
    find_library(IOKIT_LIBRARY IOKit)
    find_library(FOUNDATION_LIBRARY Foundation)
endif()

if(UNIX AND NOT APPLE)
    # If Linux, add rt and pthread
    set(rt_LIBRARIES rt)
    set(pthread_LIBRARIES pthread)
    # catkin_package(
    #     LIBRARIES ${PROJECT_NAME}
    #     INCLUDE_DIRS include
    #     DEPENDS rt pthread
    # )
# else()
#     # Otherwise normal call
#     catkin_package(
#         LIBRARIES ${PROJECT_NAME}
#         INCLUDE_DIRS include
#     )
endif()

## Sources
set(serial_SRCS
    src/serial.cc
    include/serial/serial.h
    include/serial/v8stdint.h
)
if(APPLE)
    # If OSX
    list(APPEND serial_SRCS src/impl/unix.cc)
    list(APPEND serial_SRCS src/impl/list_ports/list_ports_osx.cc)
elseif(UNIX)
    # If unix
    list(APPEND serial_SRCS src/impl/unix.cc)
    list(APPEND serial_SRCS src/impl/list_ports/list_ports_linux.cc)
else()
    # If windows
    list(APPEND serial_SRCS src/impl/win.cc)
    list(APPEND serial_SRCS src/impl/list_ports/list_ports_win.cc)
endif()


## Add serial library
add_library(serial ${serial_SRCS})
if(APPLE)
    target_link_libraries(serial ${FOUNDATION_LIBRARY} ${IOKIT_LIBRARY})
elseif(UNIX)
    target_link_libraries(serial rt pthread)
else()
    target_link_libraries(serial setupapi)
endif()

## Include headers
include_directories(include)
# include_directories(include ${COLCON_INCLUDE_DIRS} ${PCL_INCLUDE_DIRS})
# include_directories(include/${PROJECT_NAME})

# ## Uncomment for example
# add_executable(serial_example examples/serial_example.cc)
# add_dependencies(serial_example ${PROJECT_NAME})
# target_link_libraries(serial_example ${PROJECT_NAME})


add_executable(wheeltec_robot_node src/wheeltec_robot.cpp src/Quaternion_Solution.cpp) # include/Quaternion_Solution.h include/wheeltec_robot.h
target_link_libraries(wheeltec_robot_node serial)
# target_link_libraries(wheeltec_robot_node serial::serial)
ament_target_dependencies(wheeltec_robot_node ${COLCON_VARS})


# install(
#     DIRECTORY include/${PROJECT_NAME}
#     DESTINATION include
# )

# install(
#     TARGETS wheeltec_robot_node
#     EXPORT wheeltec_robot_node
#     LIBRARY DESTINATION ${COLCON_PACKAGE_LIB_DESTINATION}
#     ARCHIVE DESTINATION ${COLCON_GLOBAL_LIB_DESTINATION}
#     RUNTIME DESTINATION  ${COLCON_GLOBAL_LIB_DESTINATION}
#     INCLUDES DESTINATION include
# )

install(TARGETS wheeltec_robot_node
DESTINATION lib/${PROJECT_NAME}/)

# ament_export_targets(wheeltec_robot_node HAS_LIBRARY_TARGET)

## Tests
if(COLCON_ENABLE_TESTING)
    add_subdirectory(tests)
endif()

ament_package()
