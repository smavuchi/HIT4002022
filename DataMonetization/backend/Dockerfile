FROM python:3.9

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=./main.py
EXPOSE $PORT

CMD waitress-serve --port=$PORT run:app
