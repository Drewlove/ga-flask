
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) APIs and Requests in Flask

## Overview
This is a lesson on creating an API in Flask. Students will get to know what the common requests are (GET, POST) by creating a Flask app that does both. 


## Important Notes or Prerequisites
Students should know basic Python: writing functions that return values. Also, the following are necessary:
- Python 
- Flask `pip install Flask` 
- An internet browser (Chrome, Safari, Opera, Firefox, et al.)


## Learning Objectives
In this lesson, students will:
1. Explain what an API is
2. Create an API that makes a GET request with Flask
3. Create an API that makes a POST request with Flask
---

## Duration
30 minutes.

---

## Suggested Agenda


| Time | Activity | Purpose |
| --- | --- | --- |
| 0:00 - 0:02 | Welcome | Introduce the lesson’s objectives and agenda.|
| 0:02 - 0:10 | What are APIs? | To recap the theory behind this lesson|
| 0:10 - 0:19 | Creating a GET Request| GET request with Flask practice|
| 0:19 - 0:27 |  Creating a POST request | POST request with Flask|
| 0:27 - 0:30  | Summary | Wrap up the learning and share next steps|
---

## Differentiation and Extensions
- More advanced students may work on adding in authentication into their Flask app
- Struggling students should review the [lesson on APIs](insertlinkhere) from Day 3 of the program
- Students may also wish to explore their POST/GET requests in the Chrome Extension Postman. 
  - This is a GUI friendly version of the command line version taught in the lesson.

---

## Lesson Procedure
<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection. --->

### Welcome (2 minutes)

#### Teaching Tips:
- APIs are often a murky concept for students: they've likely heard of them, but their functionality seems to require a legion of Computer Science topics. This is untrue. Assure them this unit is self-contained and beyond baic Python abilities gained from the first 3 days, students are not required to know additional


#### Talking Points:
- Ask students if they have any familiarity interacting with APIs outside of day 3's materials
- It's **important** to explain to students that on day 3 we *called* an API. Today we are *creating* an API. 
  - This can be explained with an example like "on day 3 we were reading a book, and today, we're writing a book that others can read."
  - Calling an API allow you to retrieve data, while creating an API makes some data that you want to publish accessible

---
### What are APIs (8 minutes)

#### Teaching Tips:
- This should be a recap of Day 3, however, all of the theory in here should be sufficient as a stand-alone lesson. 

#### Talking Points:
- APIs are the vehicle that drive most of the modern web.
- Knowing how to create and consume APIs is important for a variety of coding tasks, regardless of job title.
- Flask provides an incredibly lightweight module for our purposes. 

---
### Creating a GET request in Flask (9 minutes)

#### Teaching Tips:
- This is a code along/we do. Have students open code editors and terminal, then follow along.
- We are actually doing two things at once here: we create data, and then we create an API where one could obtain that data. We focus more on the latter task, so as to emphasize creating the API.

#### Talking Points:
- This is a fantastic pattern that can be extended out to larger applications.
- Combining GET requests with templates makes for powerful applications.

---

### Creating a POST request with Flask (8 minutes)

#### Teaching Tips:
- This is a code along/we do. Students will extend the app they have been creating since the `hello_world` app. 
- Similar to the GET activity, we're creating the data that we will append to the list with a POST request.

#### Talking Points:
- This POST request is using a simple example. 
- This can extend to Create/Update data into a number of other applications: search bars, adding data into databases, and so on. 


