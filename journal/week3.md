# Week 3 — Decentralized Authentication

The authentication is going to be implemented with Amazon Cognito. Although there are many instructions and manual online, it is difficult to find instructions how to implement Cognito on backend with a custom login page instead of the Cognito hosted UI. When using Cognito, you can either manage things on client side or server side depending on the application. Traditional monolithic applications usually use serverside and modern SPA-applications client side. 

## Setup Cognito User Pool

The first step was to set up user pool on the console. To limit costs, it was better not to enable MFA and also to allow email recovery by email only (instead of SMS). There were several options that were not very clear from the beginning and had to be modified afterwards.

![user pool](user_pool.png)

After user pool created, it was time to move to Gitpod. There used to be a Cognito library for Javascript, but that library was integrated to AWS Amplify, which means now need to install the whole Amplify library in order to use Cognito. 

The first step was to install Amplify with ``npm i aws-amplify —save``, as we need it as a dependency instead of dev-dependency. After that Amplify was imported to app.js and import Amplify statement to app.js. Also configuration code was added to app.js and environment variables to Docker-compose. This code nee the user pool ID's from the AWS console from the user pool that was created earlier.

Next it was necessary to do some changes to the app in order to conditionally show components based on user being logged in or logged out. This was done in Homepagefeed component. This component already had ``useState`` which is needed to managed state. 

The first step was to import Auth from aws-amplify add then add code to check if the user is authenticated. There was originally a mock authentication implemented with cookies, so that code had to be replaced. The user also had to be passed to ``DesktopNavigation`` and DesktopSidebar`` components as these components also show different details depending whether the user is logged in or not:

``<DesktopNavigation user={user} active={'home'} setPopped={setPopped} />
<DesktopSidebar user={user} />``

Similar changed were needed in ``Profileinfo.js`` - importing Auth from aws-amplify and adding code to replace authentication done with cookies.

## Implement Custom Sign In Page

The implementation was started by importing Auth from aws-amplify and adding code to replace authentication done with cookies. The access token is stored in localStorage. There would be also other options to manage this.

In order to test the sign in functionality, a new user had to be created in the AWS console. The problem was that this user was stuck in ``for change password`` status, as the application didn't yet have the functionality to deal with this:

![change password](change_password.png)

The password status could be changed to confirmed by running a CLI command that manually confirmed the password. 

## Implement Custom Sign Up Page

The implementation steps for sign up page were similar to the sign in page. The first step was importing Auth from aws-amplify. After that code was added to replace authentication done with cookies. 

## Implement Custom Confirmation Page

Again, the implementation for confirmation page was started by importing Auth from aws-amplify. Code need to be added to replace confirmation done by cookies. There is a function that send a confirmation code to the user’s email and then checks if it is correct.

At this point the application gave an error code 'Username cannot be of email format, since user pool is configured for email alias'. It turned out that incorrect options had been selected while creating the user pool, so a new one had to be created in the console and then updated the corresponding IDs in the docker-compose -file.

Now it was possible to create a new user, receive a confirmation code via email and then confirm the user with the confirmation code directly in the UI. The user was now displayed as 'confirmed' in AWS console:

![new user](new_user.png)

## Implement Custom Recovery Page

Similar steps were still needed for the recovery page. The first step was importing Auth from aws-amplify, then adding code to send and confirm activation cod. Now it was possilbe to click 'forgot password' and get a password reset code via email.


## Verify JWT Token server side to serve authenticated API endpoints in Flask Application

When an API call is made, also the token needs to be sent with the request. The below code was added to Homefeedpage to grab the token from localStorage and pass it to backend:

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

This first produced a CORS error, which was resolved by updating CORS headers in app.py to include Authorization.

The token was now passed to backend, but further functionality had to be added for it to work. There are several ways to implement this and a few different options were explored to see which would be most suitable here. There are several extension available for this purpose, one of them being ‘Extension for Flask that adds support for AWSCognito into your application’. It is actually a server side verification and our application would only need to use parts of it as the verification is done on client side. The only functionality needed would be to validate the token. The issue with this extension was, that it requires a secret to be used at the user pool, which is not use at the user pool for Cruddur. Adding a secret would require changes to the way the application works. 

Due to above restrictions the best way was to use only some of the code from the extension. This was implemented in new file``cognito_jwt_token.py``. It took a few tried and several changes to the code to make it work. Some code from the extension's ``plugin`` and ``utils`` files had to be added as well.




## Different approaches of verifying JWTs
