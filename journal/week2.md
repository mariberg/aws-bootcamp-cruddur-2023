# Week 2 — Distributed Tracing

## Required homework

### Honeycomb

During this week live lesson we learned about Honeycomb and instrumented our backend Flask -application to use OTEL (Open Telemetry) with Honeycomb.io as the provider. We started by creating a new environment called 'bootcamp' and copying the API key from Honeycomb.io and setting that as an envinroment variable on Gitpod. We added OTEL settings in docker-compose -file. We did this for the backend now, but same could be later added for frontend -application as well. We followed instructions on Honeycomb.io to complete the installation, which required adding code to requirements.txt and App.py -files. 

We hardcodeda new span in the 'home activities' (to say  we are returning hard-coded datat) and we now had two spans visible in Honeycomb every time we make a request to that backend route:

![spans](home_activities_mock)

As I have in the previous week added a healthcheck on this endpoint, it is now sending a request to this route every 30 sec, which means there is always a new trace created. Each trace has 'count 2', which means there are two spans:

![traces](traces)

Our cloud environment is now sending standardise messages to Honeycomb.io and Honeycomb stores them in the database and gives an UI to look at them. 



### Rollbar

We configured Rollbar for our project. It is a cloud-based bug tracking and monitoring solutions, which supports multiple programming languages and frameworks. Configuring it for Flask was straightforward. The idea is, that when whenever we run into an error, we check what kind of information Rollbar can give us about the error. It will be even more useful in production, where we don't otherwise have easy access to error messages like we have in development. 

We started by creating a Rollbar account, adding blinker and rollbar to requirement.txt-file for Flask. We took a token from Rollbar account and added that as an environment variable on Gitpod. We added import statements, passed Rollbar access to token to backend-flask on docker-compose -file. and added code to app.py. and adding an endpoint that produces an error to test that Rollbar works. This is what my Rollbar account shows when a request is send to the route:

![rollbar/test](rollbar_test)

We made an additional test by breaking code in 'home activities', which produces this error in Rollbar:

![rollbar_error](rollbar_error)


### X-ray
