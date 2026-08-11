FROM node:20

RUN echo "Hello from Docker!!!"

CMD [ "echo", "Hello from the dark side of the container"]

WORKDIR /app

COPY requirements.txt .

RUN echo "Installing requirements..."

RUN pip install -r requirements.txt