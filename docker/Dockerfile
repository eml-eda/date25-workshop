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
