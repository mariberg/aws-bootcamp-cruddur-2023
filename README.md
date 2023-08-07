# FREE AWS Cloud Project Bootcamp

This application has been created while taking part in the free AWS Cloud project bootcamp by Andrew Brown / ExamPro. The starting code base [ExamPro AWS Cloud Project Bootcamp](https://github.com/ExamProCo/aws-bootcamp-cruddur-2023) has been used as a template to initially create this project. The bootcamp ran over four months during which new code was regularly committed to this repository accompanied by journal entries describing the weekly progress.

![Cruddur Graphic](_docs/assets/cruddur-banner.jpg)

![Cruddur Screenshot](_docs/assets/cruddur-screenshot.png)

## Structure of the project

The project consists of a social media application called 'Cruddur'. The users are able to message each other and they have a feed that displays messages that are relevant to them. The frontend of the project has been created with ReactJS (JavaScript). The backend has been created with Flask (Python). The project also includes a large number of bash scripts. Additionally, Ruby has been used for a few small parts of the project.

Parts of the application itself were ready when the bootcamp started, but a large part of it was completed during the bootcamp. Additionally, existing parts were modified as needed while progressing through the bootcamp. However, the main focus of the bootcamp was to deploy the application on AWS.

## AWS services that were used

The application has been deployed on AWS by utilizing several AWS services. The backend has been deployed as a **Docker** container on **ECS Fargate**.

Frontend has been deployed using **S3** and  **CloudFront**.

**X-Ray** is instrumented to be used as an observability tool. 

**Cognito** is used for decentralized authentication.

**RDS Postgres** is used as a database for the user data. **DynamoDB** is used as a single table design for the messages.

A hosted zone on **Route 53** is linked to the custom domain cloudproject.online. **Application load balancer** is used to forward requests to the frontend and backend containers.  

Serverless image processing is implemented using **API Gateway**, two **Lambda** functions, **presigned URL**, **S3** and **CloudFront**.

**CodePipeline**, **CodeBuild** and **CodeDeploy** are used for CI/CD.

The first version of the project was completed by partially clicking through the AWS console and utilising AWS CLI. During weeks 10-11, the infrastructure was re-created using **CloudFormation**. Additionally to CloudFormation, the serverless image processing (week 8) was completed with **AWS CDK**.  


## Third-party tools that were used

**Honeycomb** was used as an observability tool as an addition to AWS X-Ray mainly because it was very straightforward to instrument and easy to use.

**Rollbar** was configured to be used for monitoring and bug-tracking.

## Current status

The bootcamp has been completed and my weekly progress is documented in the below journal. Currently waiting for grading.


## Weekly journal

I have written a detailed journal for each week of the project. I have added architectural diagrams to several weekly journals in order to clarify the infrastructure that was created during that week. The journal entries contain details of the steps that were completed during the week and information about overcoming possible challenges. Some of the weekly journal entries also contain links to articles I have written about some aspects of that specific week. 

- [x] [Week 0 - Billing and Architecture](journal/week0.md)
- [x] [Week 1 - App Containerization](journal/week1.md)
- [x] [Week 2 - Distributed Tracing](journal/week2.md)
- [x] [Week 3 - Decentralized Authentication](journal/week3.md)
- [x] [Week 4 - Postgres and RDS](journal/week4.md)
- [x] [Week 5 - DynamoDB and Serverless Caching](journal/week5.md)
- [x] [Week 6 - Deploying Containers](journal/week6.md)
- [x] [Week 7 - Solving CORS with a Load Balancer and Custom Domain](journal/week7.md)
- [x] [Week 8 - Serverless Image Processing](journal/week8.md)
- [x] [Week 9 - CI/CD](journal/week9.md)
- [x] [Week 10-11 - CloudFormation](journal/week10-11.md)
- [x] [Week X - Cleanup](journal/weekX.md)

## Articles

In addition to the weekly journal, I have also written two articles about the bootcamp. In the first article about [DynamoDB week](https://blog.marikabergman.com/aws-cloud-project-bootcamp-dynamodb) I go through the main points regarding DynamoDB data modelling for our application. The main topics of the article are access patterns and the reason we choose to use a global secondary index. 

My second article about the [infrastructure as code](https://blog.marikabergman.com/aws-cloud-project-bootcamp-iac) part of our project goes through the tools that were used to provision our infrastructure. I have explained in the article the current status of the infrastructure provisioning and further steps that would be needed to fully automate it. 
