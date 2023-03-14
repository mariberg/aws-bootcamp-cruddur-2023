# Week 3 — Decentralized Authentication

The authentication for the application is going to be implemented with Amazon Cognito. Although there are many instructions and manuals online, it is difficult to find instructions on how to implement Cognito on the backend with a custom login page instead of the Cognito-hosted UI. When using Cognito, you can either manage things on the client side or server side depending on the application. Traditional monolithic applications usually use serverside and modern SPA applications client side. 

## Setup Cognito User Pool

The first step was to set up a user pool on the AWS console. To limit costs, it was better not to enable MFA and also to allow email recovery by email only (instead of SMS). There were several options that were not very clear from the beginning and had to be modified afterwards.

![user pool](user_pool.png)

After the user pool was created, it was time to move to Gitpod. There used to be a Cognito library for Javascript, but that library was integrated into AWS Amplify, which means you now need to install the whole Amplify library in order to use Cognito. 

The first step was to install Amplify with ``npm i aws-amplify —save``, as it was needed as a dependency instead of dev-dependency. After that Amplify was imported to ``app.js`` and import Amplify statement added to ``app.js``. Also, configuration code was added to ``app.js`` and environment variables to ``Docker-compose``. This code requires the user pool ID's from the AWS console from the user pool that was created earlier.

Next, it was necessary to make some changes to the app in order to conditionally show components based on the user being logged in or logged out. This was done in the ``Homepagefeed`` component. This component already had ``useState`` which is needed to manage state. 

The first step was to import Auth from aws-amplify and then add code to check if the user is authenticated. There was originally a mock authentication implemented with cookies, so that code had to be replaced. The user also had to be passed to ``DesktopNavigation`` and ``DesktopSidebar`` components as these components also show different details depending on whether the user is logged in or not:

``<DesktopNavigation user={user} active={'home'} setPopped={setPopped} />
<DesktopSidebar user={user} />``

Similar changes were needed in ``Profileinfo.js`` - importing Auth from aws-amplify and adding code to replace authentication done with cookies.

## Implementing Custom Sign-In Page

The implementation was started by importing Auth from aws-amplify and adding code to replace authentication done with cookies. The access token is stored in localStorage. There would be also other options to manage this.

In order to test the sign-in functionality, a new user had to be created in the AWS console. The problem was that this user was stuck in  'force change password' status, as the application didn't yet have the functionality to deal with this:

![change password](change_password.png)

The password status could be changed to 'confirmed' by running a CLI command that manually confirmed the password. 


## Implementing Custom Sign-Up Page

The implementation steps for the sign-up page were similar to the sign-in page. The first step was importing Auth from aws-amplify. After that code was added to replace authentication done with cookies. 


## Implementing Custom Confirmation Page

Again, the implementation for the confirmation page was started by importing Auth from aws-amplify. Code needed to be added to replace confirmation done by cookies. There is a function that sends a confirmation code to the user’s email and then checks if it is correct.

At this point the application gave an error code 'Username cannot be of email format, since user pool is configured for email alias'. It turned out that incorrect options had been selected while creating the user pool, so a new one had to be created in the console, which meant that also the corresponding IDs in the ``docker-compose`` -file had to be updated.

Now it was possible to create a new user, receive a confirmation code via email and then confirm the user with the confirmation code directly in the UI. The user was now displayed as 'confirmed' in the AWS console:

![new user](new_user.png)


## Implement Custom Recovery Page

Similar steps were still needed for the recovery page. The first step was importing Auth from aws-amplify, then adding code to send and confirm activation cod. Now it was possible to click 'forgot password' and get a password reset code via email.


## Verifying JWT Token server side to serve authenticated API endpoints in Flask Application

When an API call is made, also the token needs to be sent with the request. The below code was added to ``Homefeedpage`` to grab the token from localStorage and pass it to backend:

``
 const loadData = async () => {
    try {
      const backend_url = `${process.env.REACT_APP_BACKEND_URL}/api/activities/home`
      const res = await fetch(backend_url, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`
        },
        method: "GET"
      });
``

This first produced a CORS error, which was resolved by updating CORS headers in ``app.py`` to include Authorization.

The token was now passed to the backend, but further functionality had to be added for it to work. There are several ways to implement this and a few different options were explored to see which would be most suitable here. There are several extensions available for this purpose, one of them is called ‘Extension for Flask that adds support for AWSCognito into your application’. It is actually a server-side verification and our application would only need to use parts of it as the verification is done on the client side. The only functionality needed would be to validate the token. The issue with this extension was, that it requires a secret to be used at the user pool, which is not used at the user pool for Cruddur. Adding a secret would require changes to the way the application works. 

Due to the above restrictions, the best way was to use only some of the code from the extension. This was implemented in the new file ``cognito_jwt_token.py``. In order to do that, it was first necessary to understand the codebase and how the extension works. It took a few tries and several changes to the code to make it work. Some code from the extension's ``plugin`` and ``utils`` files had to be added as well.



## Different approaches to verifying JWTs

There are several different approaches to verifying JWTs and it is not always straightforward which approach to choose. ChatGPT suggested the following solution:

![chatGPT](chatGPT.png)

This code is a lot shorter than the one that was used for Cruddur. However, it doesn’t look like it is done purely on the front end only. Rather it seems it hits the Cognito API to get the user data. This is an extra step you don't want to do unless absolutely necessary. For this reason, the code is not the best choice in this particular situation.

AWS documentation explains that there is a library called ``aws-jwt-verify`` to validate the parameters in the token that your user passes to your app. However, this library works only for Node.js and there is no official alternative for Python. For Python, you have the option to use a community library, but you have to go through the code and understand how it works before using it - just like was done in the previously explained section for ‘Extension for Flask that adds support for AWSCognito into your application’  .  

The benefit of using your own code instead of these ready libraries is that you know what exactly your code does and in the case of Cruddur the code is also quite short and easy to maintain.

In the current solution, the JWT verification is implemented inside the app. The verification is inside its own file whereas the backend application has a ``Homeservices`` endpoint in ``app.py``, which this file connects to.

JWT verification could also be implemented as a middleware where it would be located outside of the app and all requests would pass through it. In this case, it could be implemented in its own Docker container. This means it could use NodeJS runtime and the above-mentioned AWS' own library for the verification. This container would be located next to the backend container and it could be described as a sidecar. Any request would pass through this sidecar middleware container, which could modify the request and add something to it before it reaches the backend container. 

There is also a further option, which modifies the architecture of the application by adding an AWS API Gateway to it. Each endpoint in Flask app would have a corresponding endpoint in the API Gateway. API gateway would then either have direct integration to jwt verification or alternatively, there could be a Lambda function in front of it. The Lambda function would check the verification and make API gateway return 401 error if the user is not authenticated. This implementation could initially be cost-effective, but could later become expensive as the userbase increases, especially in a case of a social media platform. Implementing it might also be too time-consuming for this bootcamp.
