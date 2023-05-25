# Week 9 — CI/CD with CodePipeline, CodeBuild and CodeDeploy

There are going to be individual CI/CD pipelines for different services. This week the pipeline for backend-flask Fargate service was created. When creating a new pipeline, a new connection called 'cruddur' to the Github repository was created. When the connection was created, the repository could be accessed from the CodePipeline. 

For the purpose of the pipeline a new branch 'prod' was created for the Github repo. 

The pipeline was first created for two stages only: source and deploy. The source was connected to the Github repository. The deploy stage obviously wouldn't work without adding a build stage first. 

The build stage was created through the CodeBuild conosle as a new project. Selected settings that we will automatically build on push and on pull_request_merged. The environment is the runtime for the build environment. (continue from vpc)

### Configuring CodeBuild Part 1

###	Configuring CodeBuild Part 2

### Configuring CodePipeline
