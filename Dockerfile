FROM ros:humble

ENV COLCON_WS=/root/colcon_ws
ENV COLCON_WS_SRC=${COLCON_WS}/src

RUN apt-get update -qq \
    && apt-get install -y \
        ros-humble-ament-cmake \
        python3-colcon-ros \
        python3-colcon-common-extensions \
        python3-colcon-pkg-config \
        python3-colcon-bash \
    && rm -rf /var/lib/apt/lists/*

COPY ./entrypoint.sh /ros2_ws_entrypoint.sh
RUN chmod a+x /ros2_ws_entrypoint.sh
ENTRYPOINT [ "/ros2_ws_entrypoint.sh" ]

WORKDIR ${COLCON_WS}
RUN mkdir -p ${COLCON_WS_SRC}
COPY ./sys_msgs ${COLCON_WS_SRC}/sys_msgs
COPY ./sys_node ${COLCON_WS_SRC}/sys_node
RUN . /opt/ros/humble/setup.sh && cd ${COLCON_WS} && colcon build
CMD [ "ros2", "run", "sys_node", "sys_node" ]