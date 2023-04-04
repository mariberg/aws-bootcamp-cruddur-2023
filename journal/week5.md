# Week 5 — DynamoDB and Serverless Caching

## Data Modelling a Direct Messaging System using Single Table Design

This application uses simple table design, which makes the data modelling quite challenging. It is crucial to have your data mapped or you will end up with something that doesn't either work or becomes very expensive. To make it as cost effective as possible, it is important to choose such a design that as much a possible of the data you need is easily available, without using GSIs (global secondary index). When starting designing the database model, the first step is to list the different access patterns. For this application there are five initial access patterns, although more might be needed to be added (such as changing a username):
- Showing a single conversation
- A list of conversations
- Creating a message
- Adding a new message to an existing message groups
- Update a message group by using DynamoDB streams

## 	Implement Schema Load Script

## 	Implement Seed Script

## Implement Scan Script

## Implement Pattern Scripts for Read and List Conversations

## Implement Update Cognito ID Script for Postgres Database

## mplement (Pattern A) Listing Messages in Message Group into Application

## 	Implement (Pattern B) Listing Messages Group into Application

## Implement (Pattern B) Listing Messages Group into Application

## Implement (Pattern C) Creating a Message for an existing Message Group into Application

## Implement (Pattern D) Creating a Message for a new Message Group into Application

## Implement (Pattern E) Updating a Message Group using DynamoDB Streams
