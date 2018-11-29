#!/usr/bin/env python

import os
from kubernetes import client, config, watch

def main():
    config.load_kube_config()
    api = client.BatchV1Api()

    # Create and configure a container
    container = client.V1Container(
        name="c",
        image="bigtexasdork/job-wq-1",
        env=[
            client.V1EnvVar(name="BROKER_URL", value="amqp://guest:guest@rabbitmq-service:5672"),
            client.V1EnvVar(name="QUEUE", value="job1")
            ]
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
        completions=8,
        parallelism=2,
        template=template
    )

    # Create the Job
    job = client.V1Job(
        metadata=client.V1ObjectMeta(name="job-wq-1"),
        spec=jobSpec
    )

    api.create_namespaced_job(
        namespace="default",
        body=job
    )

if __name__ == '__main__':
    main()