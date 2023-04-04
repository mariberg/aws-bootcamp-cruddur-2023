# Week 5 — DynamoDB and Serverless Caching

## Data modelling a direct messaging system using single table design

This application uses simple table design, which makes the data modelling quite challenging. It is crucial to have your data mapped or you will end up with something that doesn't either work or becomes very expensive. To make it as cost effective as possible, it is important to choose such a design that as much a possible of the data you need is easily available, without using GSIs (global secondary index). When starting designing the database model, the first step is to list the different access patterns. For this application there are five initial access patterns, although more might be needed to be added (such as changing a username):

- Showing a single conversation
- A list of conversations
- Creating a message
- Adding a new message to an existing message groups
- Update a message group by using DynamoDB streams

## 	Implement schema load script

This script loads your schema to DynamoDB. At the beginning of the script there is a conditional that allows us to use the script either for local develoment environment or production. Some of the default options for the schema had to be modified to be compatible with AWS free tier. For example ReadCapacityUnits and WriteCapacityUnits can't be above certain values for free tier. 


## 	Implementing seed script

The seed file for DynamoDB is written in Python and has the option to be used for either development or production. In order to create the seed file, a function in SQL is needed to get the user uuid from RDS. Once the uuid is obtained, the seed file can be used to populate the DynamoDB tables. 

The seed script has two functions, create_message_group and create_message. The function called create_message is adding a message to DynamoDB and using ‘my user’ details obtained in the above mentioned SQL query. Table name has been hardcoded to the query as there is only one table.  Function create_message_group is used to create a new message group. This function is called twice as there needs to be two message groups, one from the perspective of each user. 

The seed script also has a hardcoded conversation as mockdata to populate the message group. Seeding data like this will be done only for development and for production it would be implemented differently as write operations can end up being expensive.

## Implementing scan script

A scan file was created to easily scan the database and see what is there. This is for development only as a scan can be expensive in production. After using the seed script first, the scan option returns all data that was included in the seed script. 

## Implementing pattern scripts for read and list conversations

These two pattern scrips are actually for two of the access patterns (A and B).

The script to read a conversation is called get-conversation. There are two different options how you can filter the conversations, either looking for conversations in certain year or between certain dates. It will be decided later which of these ways is going to work better for this application. 

List-conversations is created to list all of the conversations that the user has. In this script there is also a function called get_my_user_uuid, which first get's the current user UUID as that get's updated every time the database is re-launched.

## Implement Update Cognito ID Script for Postgres Database

In order to implement the access patterns a new library file called ddb.py was created. All the functions wil be directly in this file. The table name is hard coded and this would be a problem is a separate staging environment was used in the future. 

Hardcoded mock data has been used until now for the users. However now it's time to start pulling the real user information from Cognito. 

update_cognito_user_ids file was added to db-folder. It first gets all of the users from Cognito, and the updates the user ID. This needs to be run after each setup.

After this script was working, also a function called data_message_groups in app.py could be updated from using a hardcoded handle to use the Cognito user id. 


## 	Implementing (Pattern B) listing message groups

ist_message_groups function is quite similar to the list-conversations we created earlier. The only different is that we don’t simply dump json, but we iterate through the items and do something to them 



## Implementing (pattern A) listing messages in message group



The partition key for this pattern is messageGroup_uuid as that is the most straightforward way to access messages in a certain conversation.







## Implement (Pattern C) Creating a Message for an existing Message Group into Application

## Implement (Pattern D) Creating a Message for a new Message Group into Application

## Implement (Pattern E) Updating a Message Group using DynamoDB Streams
