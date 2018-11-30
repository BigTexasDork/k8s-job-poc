#!/usr/bin/env python
import boto3
import time

def main():
    # Get the service resource
    sqs = boto3.resource('sqs', region_name='us-west-2')

    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='a-kube-test-queue.fifo')

    # Process message
    for message in queue.receive_messages(MessageAttributeNames=['Sleep']):
        # Print out the body 
        print('Processing message: {0}.'.format(message.body))

        sleep_num = 10
        if message.message_attributes is not None:
            sleep_str = message.message_attributes.get('Sleep').get('StringValue')
            if sleep_str:
                sleep_num = int(sleep_str)

        message.delete()

        print('Sleeping for {0} to simulate work.'.format(sleep_num))
        time.sleep(sleep_num)

if __name__ == '__main__':
    main()
