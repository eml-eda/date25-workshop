# DATE 2025 (W07.4)
## Pushing TinyML Forward: End-to-end In-Memory RISC-V Computing

This repository contains the notebook shown during the workshop's demo. While running the final model requires the hardware setup, the notebook can be used as an example of how to extend the MATCH compiler to support new accelerators.

To execute the notebook, please follow the instructions below.

1. Create an empty folder and clone this repository and the MATCH repository.
```bash
mkdir workshop
cd workshop
git clone https://github.com/eml-eda/date25-workshop.git
git clone https://github.com/eml-eda/match.git
```

2. Build the workshop's docker image:
```bash
docker build -t match_date25 -f date25-workshop/docker/Dockerfile .
```

3. Run the following command to mount the match folder in the docker container and build MATCH's fork of TVM. This will take a while, but is only needed the first time.
```bash
docker run -it --rm -v ./match:/match -w /match match_date25 bash -c " \
    git submodule update --init --recursive && \
    make build_tvm -j4"
```

4. Run the following command to start the docker container while mounting the workshop folder and launching Jupyter.
```bash
docker run -it --rm -p 8888:8888 -v ./match:/match -v ./date25-workshop:/date25-workshop \
    -w /date25-workshop match_date25 bash -c " \
    export TVM_HOME=/match/match-tvm && \
    export PYTHONPATH="/match:/match/match-tvm/python:/match/zigzag"
    jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"
```

5. Open the URL shown in the terminal in your browser (the one with address `http://127.0.0.1:8888/?token=...`) and open the `workshop.ipynb` notebook.
