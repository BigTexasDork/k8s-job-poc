# Kubernetes Job Test

## POC

[oneJobPerMessage.py](oneJobPerMessage.py) - This pattern creates a job for every message it submits. The job runs the container built in the [build](build) folder.  The container's entrypoint (CMD) reads one message from SQS, processes it, and exits. This pattern should (not tested yet) allow us to use [kubernetes-ec2-autoscaler](https://github.com/openai/kubernetes-ec2-autoscaler).  The kubernetes-ec2-autoscaler scales the k8s cluster based on the number of jobs pending in the cluster.  In this scenario each job has completions AND parallelism both set to 1.  This script runs correctly right now, assuming your local kubectl is configured to connect to the test cluster I've created.


[createOneJob.py](createOneJob.py) - This pattern submits all the messages, then creates a single job to process them all. In this scenario, the job has completions set to the number of messages submitted and parallelism set to the number of concurrent pods we want to run.  It would depend on k8s' [cluster-autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) which isn't job based, it is based on (TBD). This is the first iteration I wrote, based on rabbitMQ, because that's what I know.  The container in [build](build) won't support this anymore, I'd have to recreate it.