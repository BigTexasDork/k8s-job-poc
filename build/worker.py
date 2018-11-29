#!/usr/bin/env python
import boto3
import time

def main():
    # Get the service resource
    sqs = boto3.resource('sqs', region_name='us-west-2')

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='a-kube-test-queue.fifo')

    # Process message
    for message in queue.receive_messages():
        # Print out the body 
        print('Processing message: {0}'.format(message.body))

        # Let the queue know that the message is processed
        message.delete()

        # Sleep to simulate processing
        time.sleep(10)

if __name__ == '__main__':
    main()
