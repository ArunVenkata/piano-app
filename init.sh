#!/bin/bash
# sudo add-apt-repository ppa:deadsnakes/ppa
# sudo apt update
# sudo apt install python3.7
virtualenv -p python3.7 venv
# echo $PWD
source ./venv/bin/activate
pip install -r requirements.txt