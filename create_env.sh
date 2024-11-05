#!/usr/bin/bash

python3 -m venv .venv
. .venv/bin/activate

python3 -m ensurepip 
python3 -m pip install -r requirements.txt

