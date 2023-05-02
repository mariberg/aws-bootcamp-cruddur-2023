# Week 6 — Deploying Containers

This week was delivered together with week 7 so some topics are overlapping and the below topics might not have been complited exactly in this order.

There are several option to deploy containers on AWS: Lambdas, AppRunner, ECS EC2, Elastic Beantstalk, Fargate and Kubernetes. ECS EC2 was considered as an option for this bootcamp as it would be possible to utilize freetier, however you would have to manage compute and also connecting EC2 instances to Cognito is not straightforward as in EC2 the IP addresses are private, which means you would have to use NAT Gateway, which would create costs. In the end a decition was made to use Fargate serverless containers even though there will be some spend, but the solution is fully managed so you don't have to manage compute nad it is also a good migration path to Kubernetes. 

### Provision ECS Cluster

Before starting with ECS, a way to make health checks was needed. A health-check for the Flask app was implemented by adding a simple endpoint to app.py and adding a Python script for it. 

After that an ECS cluster was provisioned for the Cruddur application. An ECS cluster is a grouping of containers that are used to run and manage containerized applications. It can contain either ECS EC2 instances or AWS Fargate tasks. The ECS cluster was created with a simple AWS CLI command:

```
aws ecs create-cluster \
--cluster-name cruddur \
--service-connect-defaults namespace=cruddur
```

After this command was run, there was an ECS cluster visible in the AWS ECS console, however it was empty without no infrastructure. 

### Create ECR repo and push image for backend-flask

To deploy an application on ECS, you will need to have images in AWS ECS (elastic container registry). An ECR repository was created through AWS Cli. The URI of the repository was then added as an environment variable on Gitpod.

For Cruddur a base Python image from Dockerhub is used, however it was better to have this image in ECR as using Dockerhub would just another point of failure in case there are connectivity issues. The slim-buster image was pulled from Docker hub, tagged and pushed to ECR. The Dockerfile was then updated to use the image from ECR instead of Dockerhub.

Next another ECR repo was created for backend-flask. This image was not only pulled as the previous image, but it actually had to be build:

```
docker build -t backend-flask .
```

It was again tagged and pushed to ECR and the ECR URI was saved as an environent variable on Gitpod.

### Deploy Backend Flask app as a service to Fargate

The first step in to create a task definition file, which is a little bit like a docker-compose file. It has a family name (backend-flask) and you only have one container in a single task definition file. You could add there multiple containers in theory, but you would be coupling them. That solution would make sense only for a sidecar (containers that share the same resources should be listed in the same task definition file). You add the health check on the task definition file, and also the task role (the role the container will have when it's running) and the execution role (the role it has when it executes). You also need to define CPU and memory within certain intervals when you use Fargate, opposed to EC2 where you could choose whatever you want. The roles were created through the console after having some issues with AWS cli and thoseat the moment give two priviledged access which has to be corrected later when using CloudFormation.

At this point also a way to store secrets was needed. As AWS secrets manager costs money, the decision was made to use AWS parameter store. Several environment variables such as AWS access keys and Rollbar & Honeycomb access tokens were passed from Gitpod to Parameter store. 

For the task definition a file called ``backend-flask.json`` was created in a ``task-definitions`` folder. By running a simple AWS CLI command a task definition was added to ECS:

```
aws ecs register-task-definition --cli-input-json file://aws/task-definitions/backend-flask.json
```

Whenever the task-definition is updated, this command has to be re-run.

The last step before being able to create a container, was creating a security groups. AWS CLI command was used to get the default VPC ID from AWS and then another CLI command to create a security group. The first try of creating a service run into a 404 permission error, which meant the permissions had to be tweaked a few times before it worked. 

Next a way to log into a backend container was needed in order to make debugging easier. A bash sript was added in the ECR folder. I had first issues logging into my container and kept receiving this error:

![InvalidParameterException.png](assets/InvalidParameterException.png)

I troubleshooted this by running ``aws ecs describe-tasks``, which showed that executeCommand -flag was set up as 'false'. However my in the task definition file the enableExecuteCommand had been set up as 'true'. I spend some time on this, which helped me to understand the whole process and all the steps we had taken before. I think in the end the issue was that I had been looking at a task that didn't actually use the updated task defition and for this reason there was a discrepancy. By running update service and forcing a new deployment I was able to get my task have the enable execute command as 'true'. Loggin in to the container worked now:

![login backend](assets/backend-login.png)

Now when inside the container, it was possible to test the RDS container with a bash script that was created for this purpose. The connection just hang, which meant the security group had to be updated to allow the container to access it. The security group of the ECS service was added as an inbound rule to the security group of RDS database and after that the ``bin/db/test`` script could be run successfully. 

## Add service connect to backend-flask

### Create ECR repo and push image for fronted-react-js
### Deploy Frontend React JS app as a service to Fargate

### Configure task definitions to contain X-ray and turn on Container Insights
### Change Docker Compose to explicitly use a user-defined network
### Create a Dockerfile specifically for production use case
### Using Ruby generate out env dot files for Docker using erb-templates
