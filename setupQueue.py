#!/usr/bin/env python
import boto3
from kubernetes import client, config, watch

def createJob(api, counter):
    jobName = f"job-search-worker-{counter}"

    # Create and configure a container
    container = client.V1Container(
        name="c",
        image="bigtexasdork/job-search-worker"
    )

    # Create and configure a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "search-worker"}),
        spec=client.V1PodSpec(
            containers=[container],
            restart_policy="OnFailure"
        )
    )
    
    # Create and configure a Job spec
    jobSpec = client.V1JobSpec(
        completions=1,
        parallelism=1,
        template=template
    )

    # Create the Job
    job = client.V1Job(
        metadata=client.V1ObjectMeta(name=jobName),
        spec=jobSpec
    )

    api.create_namespaced_job(
        namespace="default",
        body=job
    )

    print(f"Create job: {jobName}")

def main():
    config.load_kube_config()
    api = client.BatchV1Api()

    sqs = boto3.resource('sqs')

    queue = sqs.get_queue_by_name(QueueName='a-kube-test-queue.fifo')

    cntr = 0
    for msg in ["one", "two", "three", "four", "five", "six", "seven", "eight"]:
        cntr += 1
        response = queue.send_message(
            MessageBody=msg,
            MessageGroupId="travelers"
        )

        print(response.get('MessageId'))
        print(response.get('MD5OfMessageBody'))
        createJob(api, cntr)

if __name__ == '__main__':
    main()
