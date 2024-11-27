FROM python:3.12-alpine
RUN pip install -r requirements.txt
RUN apk add --no-cache gcc musl-dev linux-headers
RUN python download.py \
&& sudo python setup.py build \
&& sudo python setup.py install \
&& pip install safetensors \
&& pip install torch

RUN python ./scripts/merge_files.py