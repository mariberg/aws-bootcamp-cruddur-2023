# FREE AWS Cloud Project Bootcamp

This application has been created while taking part to the free AWS Cloud project bootcamp by Andrew Brown / ExamPro. The starting code base [ExamPro AWS Cloud Project Bootcamp](https://github.com/ExamProCo/aws-bootcamp-cruddur-2023) has been used as a template to initially create this project. The bootcamp ran over the course of four months during which new code was regularly committed to this repository.

## Structure of the project

The projects consists of a social media application called 'Cruddur'. The users are able to message each other and they have a feed that displays messages that are relevant to them. Parts the application itself were ready when the bootcamp started, but a large part of it was also completed and existing parts modified during the bootcamp, although the bootcamp was mainly focused on deploying the application on AWS.

The frontend of the project has been created with ReactJS. The backend has been created with Flask. 

## AWS services that were used

The application has been deployed on AWS by utilizing several AWS services. The frontend and backend have both been deployed as Docker containers on **ECS Fargate. 

**X-Ray** was instrumented to be used as an observability tool. 

**Cognito** was used for decentralized authentication.

**RDS Postgres** was used as a database for the user data. **DynamoDB** was used as a single table design for the messages.

**Application load balancer**, **Route 53**

Serverless image processing was used by utilizing **API Gateway**, two **Lambda** functions, **presigned URL**, **S3** and **CloudFront**.

**CodePipeline**, **CodeBuild** and **CodeDeploy** were used for CI/CD.

## Infrastructure as code

The serverless image processing (week 8) was completed with **AWS CDK**. **CloudFormation** was used for all other infrastructure (week 10-11).


## Third party tools that were used during the project

**Honeycomb** was used as an observability tool as an addition to AWS X-Ray mainly because it was very straightforward to instrument and easy to use.

**Rollbar** was configured to be used for monitoring and bug-tracking.


## Journaling for weekly progress of the project

I have written a detailed journal for each week of the project. I have added to several journal entries architectural diagrams in order to clarify the infrastructure that was created during the week. The journal entries contain details of the steps that were completed during the week and information about overcoming possible challenges. Some of the weekly journal also contain links to articles I have written about some aspects of that specific week. 

- [ ] [Week 0 - Billing and Architecture](journal/week0.md)
- [ ] [Week 1 - App Containerization](journal/week1.md)
- [ ] [Week 2 - Distributed Tracing](journal/week2.md)
- [ ] [Week 3 - Decentralized Authentication](journal/week3.md)
- [ ] [Week 4 - Postgres and RDS](journal/week4.md)
- [ ] [Week 5 - DynamoDB and Serverless Caching](journal/week5.md)
- [ ] [Week 6 - Deploying Containers](journal/week6.md)
- [ ] [Week 7 - Solving CORS with a Load Balancer and Custom Domain](journal/week7.md)
- [ ] [Week 8 - Serverless Image Processing](journal/week8.md)
- [ ] [Week 9 - CI/CD](journal/week9.md)
- [ ] [Week 10-11 - CloudFormation](journal/week10.md)
- [ ] [Week X - Cleanup](journal/week11.md)
