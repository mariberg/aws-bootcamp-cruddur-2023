# Week 2 — Distributed Tracing

## Required homework

### Honeycomb

During this week live lesson we learned about Honeycomb and instrumented our backend Flask -application to use OTEL (Open Telemetry) with Honeycomb.io as the provider. We started by creating a new environment called 'bootcamp' and copying the API key from Honeycomb.io and setting that as an envinroment variable on Gitpod. We added OTEL settings in docker-compose -file. We did this for the backend now, but same could be later added for frontend -application as well. We followed instructions on Honeycomb.io to complete the installation, which required adding code to requirements.txt and App.py -files. 

We hardcodeda new span in the 'home activities' (to say  we are returning hard-coded datat) and we now had two spans visible in Honeycomb every time we make a request to that backend route:

![spans](home_activities_mock.png)

As I have in the previous week added a healthcheck on this endpoint, it is now sending a request to this route every 30 sec, which means there is always a new trace created. Each trace has 'count 2', which means there are two spans:

![traces](traces.png)

Our cloud environment is now sending standardise messages to Honeycomb.io and Honeycomb stores them in the database and gives an UI to look at them. 

### X-ray

Also X-ray will be used in this project. It is not as straighforward to configure as Honeycomb and there were a lot more steps and troubleshooting required. We started by adding aws-xray-sdk library to requirement for backend and adding code to App.py. A file for sampling (xray.json) waas added to the root of the project. A new x-ray group was then added via aws xray sdk and the group was visible in AWS console:

![xray_console](xray_console.png)

Additionally a sampling rule was created through sdk, as it is important to determine hwat kind of data you want to collect as collecting everything would be too much to go through and might end up creating additional costs. 

For setting up X-ray daemon as a container, we were using a docker image from Dockerhub. the image is maintained by AWS. The image was added to the docker-compose -file. Also environment variables for backend-flask were added in docker-compose. 

After the container was run and a request to our API endpoint was done, we could see the following logs for the x-ray container. It was now sending 'segments', which are similar to traces in Honeycomb:

![xray segments](xray_segments.png)

The segments were visible in the AWS console:

![segments in console](xray_segment_console.png)

X-ray captures were a feature we could add to routes on app.py. A custom name can be give to these routes and the given route will be visible in the console when a request is sent to the route:

** add pic of captures

** add details about subsegment

### Rollbar

We configured Rollbar for the project. It is a cloud-based bug tracking and monitoring solutions, which supports multiple programming languages and frameworks. Configuring it for Flask was straightforward. The idea is, that when whenever we run into an error, we check what kind of information Rollbar can give us about the error. It will be even more useful in production, where we don't otherwise have easy access to error messages like we have in development. 

We started by creating a Rollbar account, adding blinker and rollbar to requirement.txt-file for Flask. We took a token from Rollbar account and added that as an environment variable on Gitpod. We added import statements, passed Rollbar access to token to backend-flask on docker-compose -file. and added code to app.py. and adding an endpoint that produces an error to test that Rollbar works. This is what my Rollbar account shows when a request is send to the route:

![rollbar/test](rollbar_test.png)

We made an additional test by breaking code in 'home activities', which produces this error in Rollbar:

![rollbar_error](rollbar_error.png)


### CloudWatch Logs


## Homework challenges

As a challenge this week I implemented another Honecomb customer span. I implemented in 'notifications' service in a similar way we implemented the span in home activities. It creates a span when we return mock data for notifications:

** add screenshot

As observability is such a crucial topic, I spend this week a lot of time just learning more about the tools we are using and the background why we have chosen to use them. I am planning to complete more challenges around this topic later when I'm able to.
