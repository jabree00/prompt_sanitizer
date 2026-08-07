#!/bin/sh 
sudo apt update 
sudo apt upgrade 
sudo apt install python3 python3-pip 
python3 -m venv .venv 
source .venv/bin/activate
pip install -r requirements.txt
pip install -U pip setuptools wheel 
pip install spacy 
python -m spacy download en_core_web_sm