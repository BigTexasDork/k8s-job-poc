# Specify BROKER_URL and QUEUE when running
FROM alpine:3.7
RUN apk add --no-cache python py-pip
RUN pip install --upgrade pip boto3

COPY ./worker.py /worker.py

CMD  /worker.py
