#! /bin/bash
cd ..

python3 -m venv venv
source venv/bin/activate
pip install browser-use
playwright install