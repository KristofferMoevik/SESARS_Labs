FROM althack/ros2:humble-dev 

# ** [Optional] Uncomment this section to install additional packages. **
#
# ENV DEBIAN_FRONTEND=noninteractive
# RUN apt-get update \
#    && apt-get -y install --no-install-recommends <your-package-list-here> \
#    #
#    # Clean up
#    && apt-get autoremove -y \
#    && apt-get clean -y \
#    && rm -rf /var/lib/apt/lists/*
# ENV DEBIAN_FRONTEND=dialog

# Set up auto-source of workspace for ros user
RUN 
ARG WORKSPACE
RUN echo "if [ -f ${WORKSPACE}/install/setup.bash ]; then source ${WORKSPACE}/install/setup.bash; fi" >> /home/ros/.bashrc

# Get gazeebo stuff
# RUN sudo apt-get update
# RUN rosdep update
# RUN ls
# RUN cd src/lab
# RUN rosdep install --from-paths src --ignore-src -y

# RUN sudo apt install ros-humble-turtlesim
# RUN export TURTLEBOT3_MODEL=burger
# RUN sudo apt install -y xterm