# Week 1 — App Containerization


## Required homework

Our required homework this week included containerizing our application (frontend and backend), making additions to frontend and backend applications and making sure we are able to run DynamoDB and Postgres containers. Below are the steps I completed for the required homework:

### Running frontend and backend locally on Gitpod

To run the backend locally, we copied the commands from the Dockerfile, first installing pip and then running command for flask. We also had to set the environment variables (frontendurl & backendurl) to * or otherwise we kept getting 404 error. We afterwards had to delete the environment variables as we started working on the actual Docker app.

### Containerize Application (Dockerfiles, Docker Compose)

We first created the container for backend with command ``docker build -t  backend-flask ./backend-flask``. This command first pulled the image and then built the container. To run the container, we used command ``docker run --rm -p 4567:4567 -it -e FRONTENT_URL='*' -e BACKEND_URL='*' backend-flask``, which first set the environment variables for the container allowing us to run it. 

We did the same for frontend - created for it it's own dockerfile, which allowed us to run the container.

To run the above containers like this, would mean that we would enter several commands for running each individual container. To make this whole process easier, we added a compose-compose.yml file at the root of the project. We were now able to run the command ``docker compose up``, 

### Document the Notification Endpoint for the OpenAPI Document

We are using openAPI, which we can import to automatically create the AWS API gateway at the later stage of the project. Open API has also other benefits, such as a preview that helps us to easily get an overview of all endpoints. 

We added a new endpoint to the openapi-3.0.yml -file.

ADD SCREENSHOT HERE.


### A Flask Backend Endpoint for Notifications

We added a new route on the app.py file and created a new service called notifications_activities.py.

SCREENSHOTS?

### React Page for Notifications

For React, we first added a new route for notifications on App.js -file. We added a file called NotificationsFeedPage.js to pages. We could reuse the code from HomeFeedPage.js as it works very similarly, only the data is different, which meant we simply changed the endpoint for backend.

### Run DynamoDB Local Container and ensure it works

## Run Postgres Container and ensure it works

## Homework challenges
