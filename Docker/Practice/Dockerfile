FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN echo "Installing requirements..."

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]