# Starting from Ubuntu 22.04
FROM ubuntu:22.04
SHELL ["/bin/bash", "-c"]
# Setting values for tzdata
ENV DEBIAN_FRONTEND=noninteractive
# General
RUN apt update
# utility
RUN apt install -y vim git
 
RUN apt install -y python3 python3-pip python3-dev python3-setuptools gcc-11 libtinfo-dev zlib1g-dev build-essential cmake libedit-dev libxml2-dev llvm-14
 
RUN pip3 install "setuptools>=65.5" pyyaml "numpy<2.0" mako typing-extensions psutil scipy decorator attrs pybind11 networkx sympy matplotlib onnx tqdm multiprocessing_on_dill notebook
 
# Setting TVM and Python path environment variables
ENV TVM_HOME=/match/match-tvm
ENV PYTHONPATH="/match:/match/match-tvm/python:/match/zigzag"
ENV TVM_NCORES_INSTALL=4
 
# Create a non-root user with same UID/GID as host user
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN if getent group ${GROUP_ID}; then \
        echo "Group with ID ${GROUP_ID} already exists"; \
        existing_group=$(getent group ${GROUP_ID} | cut -d: -f1); \
        useradd -m -u ${USER_ID} -g ${existing_group} -s /bin/bash matchuser && \
        export USER_GROUP=${existing_group}; \
    else \
        groupadd -g ${GROUP_ID} matchuser && \
        useradd -m -u ${USER_ID} -g matchuser -s /bin/bash matchuser && \
        export USER_GROUP=matchuser; \
    fi && \
    mkdir -p /match /date25-workshop && \
    chown -R matchuser:$(getent group ${GROUP_ID} | cut -d: -f1) /match /date25-workshop

# Set USER command to use the new user
USER matchuser