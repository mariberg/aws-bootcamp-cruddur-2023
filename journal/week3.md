# Week 3 — Decentralized Authentication

The authentication is going to be implemented with Amazon Cognito. Although there are many instructions and manual online, it is difficult to find instructions how to implement Cognito on backend with a custom login page instead of the Cognito hosted UI. When using Cognito, you can either manage things on client side or server side depending on the application. Traditional monolithic applications usually use serverside and modern SPA-applications client side. 

## Setup Cognito User Pool

The first step was to set up user pool on the console. To limit costs, it was better not to enable MFA and also to allow email recovery by email only (instead of SMS). There were several options that were not very clear from the beginning and had to be modified afterwards.

![user pool](user_pool.png)

After user pool created, it was time to move to Gitpod. There used to be a Cognito library for Javascript, but that library was integrated to AWS Amplify, which means now need to install the whole Amplify library in order to use Cognito. 

The first step was to install Amplify with ``npm i aws-amplify —save``, as we need it as a dependency instead of dev-dependency. After that Amplify was imported to app.js and import Amplify statement to app.js. Also configuration code was added to app.js and environment variables to Docker-compose. This code nee the user pool ID's from the AWS console from the user pool that was created earlier.

Next it was necessary to do some changes to the app in order to conditionally show components based on user being logged in or logged out. 

## Implement Custom Signin Page

## Implement Custom Signup Page

## Implement Custom Confirmation Page

## Implement Custom Recovery Page

## Different approaches of verifying JWTs
