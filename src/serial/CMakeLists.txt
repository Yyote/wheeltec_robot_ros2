cmake_minimum_required(VERSION 2.8.3)
project(serial)

cmake_policy(SET CMP0057 NEW)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# find_package(rt REQUIRED)
# find_package(pthread REQUIRED)

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
add_library(${PROJECT_NAME} ${serial_SRCS})
if(APPLE)
    target_link_libraries(${PROJECT_NAME} ${FOUNDATION_LIBRARY} ${IOKIT_LIBRARY})
elseif(UNIX)
    target_link_libraries(${PROJECT_NAME} rt pthread)
else()
    target_link_libraries(${PROJECT_NAME} setupapi)
endif()

# add_library(${PROJECT_NAME} ${serial_SRCS})

## Include headers
include_directories(include)

ament_export_targets(${PROJECT_NAME} HAS_LIBRARY_TARGET)

install(
    DIRECTORY include/${PROJECT_NAME}
    DESTINATION include
)

install(
    TARGETS ${PROJECT_NAME}
    EXPORT ${PROJECT_NAME}
    LIBRARY DESTINATION ${COLCON_GLOBAL_LIB_DESTINATION}
    ARCHIVE DESTINATION ${COLCON_GLOBAL_LIB_DESTINATION}
    RUNTIME DESTINATION  ${COLCON_GLOBAL_BIN_DESTINATION}
    INCLUDES DESTINATION include
)

## Uncomment for example
add_executable(serial_example examples/serial_example.cc)
add_dependencies(serial_example ${PROJECT_NAME})
target_link_libraries(serial_example ${PROJECT_NAME})

# ## Install executable
# install(TARGETS ${PROJECT_NAME}
#     ARCHIVE DESTINATION ${COLCON_PACKAGE_LIB_DESTINATION}
#     LIBRARY DESTINATION ${COLCON_PACKAGE_LIB_DESTINATION}
#     RUNTIME DESTINATION ${COLCON_GLOBAL_BIN_DESTINATION}
# )

# ## Install headers
# install(FILES include/serial/serial.h include/serial/v8stdint.h
# #   DESTINATION ${COLCON_PACKAGE_INCLUDE_DESTINATION}/serial)
#   DESTINATION ${COLCON_PACKAGE_LIB_DESTINATION}/serial)

## Tests
if(COLCON_ENABLE_TESTING)
    add_subdirectory(tests)
endif()

ament_package()