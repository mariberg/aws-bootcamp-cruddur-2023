# Week 4 — Postgres and RDS

## Create RDS Postgres Instance

The RDS instance was provisioned through the AWS CLI with this command:

``
aws rds create-db-instance \
  --db-instance-identifier cruddur-db-instance \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --engine-version  14.6 \
  --master-username root \
  --master-user-password password \
  --allocated-storage 20 \
  --availability-zone eu-west-2a \
  --backup-retention-period 0 \
  --port 5432 \
  --no-multi-az \
  --db-name cruddur \
  --storage-type gp2 \
  --publicly-accessible \
  --storage-encrypted \
  --enable-performance-insights \
  --performance-insights-retention-period 7 \
  --no-deletion-protection
  ``
 
 It is important to note, that many of the selected options are not security best practises, as it was important to keep the costs down during this project and stay withing free tier whenever possible. In production, you would want tot use  for example backups, deletion protection and AWS secret manager to store passwords. In production the database should also not be made publicly-accessible, although during this project the security group of the subnet is gong to keep us protected even when the URL is exposed. 
 
 The new database was no visible in AWS console:
 
 ![RDS instance](assets/RDS_instance.png)

This instance can be temporarily stopped through the AWS console for 7 days to save costs.

!!!!!!!!!!!! Programmatically update a security group rule

## Create a schema SQL file by hand

A new folder called ``db`` was created for backend and within it file ``schema.sql``.  This file creates two tables for our schmema: users and activities. The following command creates the schema locally:

``psql -Upostgres cruddur < db/schemal.sql -h localhost -U postgres``

## Work with UUIDs and PSQL extensions

Extension UUID is call to obscure the user ids. Using chronological numbers is usually not good idea as this would allow anyone to easily check how many registered users you have. This command added in the beginning of ``schema.sql``:

``CREATE EXTENSION IF NOT EXISTS "uuid-ossp";``

## Bash scripting for common database actions

A new folder called ``bin` was created for database operations bash scripts. The first bash scripts were created for creating a database, dropping a databse and schema load. This files are not executable by default, so a command had to be run to make these files executable:

![bash executable](assets/bash_executable.png)

When the files were executable, a new database could simply be created by running ``./bin/db-create`` in the terminal and dropped by running ``./bin/db-drop``.

In schema-load we used 'realpath': ``schema_path="$(realpath .)/db/schema.sql"``, which is a hand way of getting your path where you are running the command and it is used a lot in bash scripts. 

An if-statement was also added to schema-load in order to run the command either in dev or prod environment. 

``db-connect`` was created to easily connect to the database and seed.sql to add some seed data (mock data) to the dev database.

Finally file ``db-setup`` was created to automatically run all bash commands, so that you don't have to manually run them every time the project is started. This is something that naturally wouldn't be done in production.

## Install Postgres Driver in Backend Application

Now that the table were created, it was possible to start writing SQL commands. However, for that a driver for PostgreSQL called ``psycopg`` had to be installed. Several things were added to ``requiremtns.txt`` -file:
- connection pool: idea is to re-use connections instead of creating new ones every time
- using Lambda would create a new connection everytime it is run, which would required using RDS proxy in order to use a connectition pool. However when ECS is used and containers are run only for a certain amount of time, it is possibly to take advantage of connectiong pooling without needing RDS proxy.
- a new file called ``db.py`` was created to create a new connection. The connectiton ULR was also added to docker-compose.
- imported the pool in ``homeactivities`` and added code to use the pool connection. The originally used mock data was removed.


## Operate common SQL commands

The first SQL query was now working:

![sql query](assets/sql_query.png)

It as now updated to actual SQL query instead of the wildcard. It has a join to the users table:

![join query](assets/join_query.png)

Now also the username is visible:

![query with username](assets/query_with_username.png)


## Connect Gitpod to RDS Instance

In order to connect Gitpod to RDS instance, we had to create a connection URL that contained the database endpoint URL taken from AWS console and save that as an environment variable. The security group had to also be updated as the default settings allow inbound traffic only from the same security group. An inbound rule had to be created for the Gitpod IP address. A handy way of finding the Gitpod IP address was running command ``curl ifconfig.me``

It was possible to update the security group directly in AWS console, however the issue with Gitpod is that the IP address is going to change every time Gitpod is re-launched. In order to faciliate this the security group ID and SG rule group ID had to be copied from the AWS console and saved as environment variables. The following CLI can be run to update the IP address for the security group rule:

``
aws ec2 modify-security-group-rules \
--group-id $DB_SG_ID \
--security-group-rules "SecurityGroupRuleId=$DB_SG_RULE_ID,SecurityGroupRule={Description=GITPOD,IpProtocol=tcp,FromPort=5432,ToPort=5432,CidrIpv4=$GITPOD_IP/32}"
``

To run this command automatically, a new file called ``rds-update-sg-rule`` was created. The following command in ``.gitpod.yml`` now saves the IP address and runs the rule everytime Gitpod is re-launched:
 
![gitpod yml](assets/gitpod_yml.png)

Now after swapping the connection URL to producting URL in docker-compose, Gitpod was connected to AWS RDS database. Schema could be created by running ``./bin/db-schme-load prod``, however no data could be seen at the frontend as the production database is literally empty. 

## Create Congito Trigger to insert user into database

In order to test the production database, a Lambda function is needed to help. It will probably be very similar to a Postgres driver that will be used later in the project. 
- this Lambda function is used only for development
- it was created manually in AWS console
- code for Lambda was saved in ``cruddur-post-confirmation.py``
- environment variable that was needed for Lambda: Postgres URL
- a Lambda layer was added - psycopg2 python postgresql client library
- added to Cognito a Lambda trigger
- Lambda also needed a VPC to work. And for VPC a new permission policy was needed:

![permission policy](assets/permission_policy.png)



## Create new activities with a database insert

-- Check where these belong?




## Implement a postgres client for python using a connection pool
## Implement a Lambda that runs in a VPC and commits code to RDS
## Work with PSQL json functions to directly return json from the database
## Correctly sanitize parameters passed to SQL to execute
