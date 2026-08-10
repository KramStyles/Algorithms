FROM python:3.8
# tells Python to print its output (like print() statements and logs) straight to the terminal screen immediately.
ENV PYTHONUNBUFFERED=1
# No need to use RUN mkdir /code as WORKDIR creates and sets
WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/