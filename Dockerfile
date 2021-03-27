FROM python:3.9-slim
COPY . /calendar-util
WORKDIR /calendar-util
RUN python -m pip install --upgrade pip
RUN pip install -r requirement.txt
RUN pytest -k pytest
RUN python -m unittest discover
