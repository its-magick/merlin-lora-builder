#!
pip install -r requirements.txt
python download.py
python setup.py build
python setup.py install
pip install safetensors
pip install torch
python ./scripts/merge_files.py
