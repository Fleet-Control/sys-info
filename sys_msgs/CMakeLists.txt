cmake_minimum_required(VERSION 3.8)
project(sys_msgs)
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/NetworkAddress.msg"
  "msg/NetworkDevice.msg"
  "srv/NetworkInfo.srv"
  "srv/SystemInfo.srv"
  DEPENDENCIES
)
ament_package()
