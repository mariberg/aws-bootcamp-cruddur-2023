# Week 1 — App Containerization


## Required homework

Our required homework this week included containerizing our application (frontend and backend), making additions to frontend and backend applications and making sure we can run DynamoDB and Postgres containers. Below are the steps I completed for the required homework:

### Running frontend and backend locally on Gitpod

To run the backend locally, we copied the commands from the Dockerfile, first installing pip and then running the command for flask. We also had to set the environment variables (frontendurl & backendurl) to * or otherwise, we kept getting 404 error. We afterwards had to delete the environment variables as we started working on the actual Docker app.

### Containerize Application (Dockerfiles, Docker Compose)

We first created the container for backend with command ``docker build -t  backend-flask ./backend-flask``. This command first pulled the image and then built the container. To run the container, we used the command ``docker run --rm -p 4567:4567 -it -e FRONTENT_URL='*' -e BACKEND_URL='*' backend-flask``, which first set the environment variables for the container allowing us to run it. 

We did the same for frontend - created for it its own dockerfile, which allowed us to run the container.

To run the above containers like this, would mean that we would enter several commands for running each individual container. To make this process easier, we added a compose-compose.yml file at the root of the project. We were now able to run the command ``docker compose up``, 

### Document the Notification Endpoint for the OpenAPI Document

We are using openAPI, which we can import to automatically create the AWS API gateway at a later stage of the project. Open API also has other benefits, such as a preview that helps us easily get an overview of all endpoints. 

We added a new endpoint to the openapi-3.0.yml -file.

![openApi](assets/openapi_notifications.png)


### A Flask Backend Endpoint for Notifications

We added a new route on the app.py file and created a new service called notifications_activities.py.


### React Page for Notifications

For React, we first added a new route for notifications on App.js -file. We added a file called NotificationsFeedPage.js to the pages. We could reuse the code from HomeFeedPage.js as it works very similarly, only the data is different, which meant we simply changed the endpoint for the backend.

![notifications React](assets/notifications.png)

### Run DynamoDB Local Container and ensure it works

We started by adding DynamoDB local to the docker-compose.yml -file. Now running ``docker compose up``creates also a container for DynamoDB. We made sure that DynamoDB works by creating a table and items.

### Run Postgres Container and ensure it works

We added Postgres to the docker-compose.yml -file. We also added a volume for Postgres at the bottom of the docker-compose.yml. Now running ``docker compose up``run also a container for Postgres. We used a database connection extension for creating a new connection:

![postgres_connection](assets/postgres_connection.png)

After the connection had been established, we connected to psql client with command ``psql -Upostgres --host localhost``. We were now inside a postgres container and could start entering postgres commands.

We had in total four containers running:

![containers](assets/containers_running.png)

## Homework challenges

### Implement a health check in the Docker-compose file

I implemented health checks for frontend and backend in the Docker-compose file. For backend, I first had to install curl as that was needed to run the healthcheck. This was done in the backend Dockerfile. With `docker ps` -command I could see that both containers had healthy status.

![healthchecks](assets/healthchecks.png)


### Run the same containers on my local machine

As an additional challenge, I ran the same containers on my local machine. This was easy to implement, as I had already installed the Docker desktop. Only some changes to URL's in the Docker-compose -file were needed.  

![containers_local](assets/containers_local.png)

![backend_localhost](assets/backend_localhost.png)

![frontend_localhost](assets/frontend_localhost.png)

