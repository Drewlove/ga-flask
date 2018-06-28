 <!---
Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack @annazocher
--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Flask - Instructor Notes

## Overview
Lesson goal: to teach students the who, what, when where of Flask - what it is, why we are using it, and how to use it. We start by talking about the history of Flask and connect that to what web frameworks are. We then walk through a couple real world examples of Flask and why developers use it.

## Important Notes or Prerequisites
- *If we decide to teach venv*: make sure students activate venv before any local development/installing flask.
    + They will then need to deactivate before running Flask

## Learning Objectives
In this lesson, students will:
- learn about web frameworks
- write a basic Flask app

## Duration
45 minutes.

---

## Suggested Agenda

| Time | Activity | Purpose |
| --- | --- | --- |
| 0:00 - 0:02 | Welcome | Introduce the lesson objectives and agenda.|
| 0:02 - 0:07 | History of Flask + What is Flask | What is Flask, and why do we have it, what is a web framework|
| 0:07 - 0:10 | Real World Flask | Walk through a couple realworld Flask apps and why these apps use Flask|
| 0:10-20  | Demo 1 | Lead demo of main, basic, Flask app + walk through slides on codebreakdown|
| 0:20-0:30 | Codealong 1 | Lead codealong for students to build Flask app locally|
| 0:30 - 0:40 | Run Flask App | Demo running Flask app locally on machines; troubleshoot any student issues|
| 0:40 - 0:45 | Recap | Recap everything we have learned, and tie together what a web app is to what we did|


## Materials and Preparation
- N/A

---

## Lesson Procedure

### Flask Discussion (10 minutes)

#### Teaching Tips:
- Goal is for students to understand what web frameworks are/what web apps are
- What is Flask and why we use it
- How Flask works

#### Talking Points:
- Open lesson by describing what they are going to do (build a flask app!), and why this is so exciting (we are using Flask to actually put your stuff on the internet!)
- Highest level overview of Flask
- Review history of Flask as described on slide, and how Werkzeug (connection library) and Jinja (templating library) make the basis of Flask/why a web app would want/need these two things.
- What is Flask? - flask is a web framework. What is a web framework? A written library of code that helps us build web apps.
- Review what web app is, and use this opportunity to review what the client-server relationship is (maybe draw out diagram on board to review?)
- Why we use a lighter web framework like Flask
- Use this to transition to real world flask apps
- Open pinterest or instagram web platforms **(will have to login to demo)**
- Talk about how these sites work (lots of interaction + data), and why it is helpful to use flask for these (get to focus on the interactivity/data, and not just getting the thing up on to the internet+staying there)

### Write Basic Flask App (20 minutes)

#### Teaching Tips:
- up to you wether you want to demo locally or in repl
    *if locally, use code in demo folder*

#### Talking Points:
- walk through demo code of a basic Flask app
- use opportunity to review what library is and what Class is
- walk through how we get to hello world message
- lead code along locally on computer to have students make their own version of this basic application.py


### Run Basic Flask App (10 minutes)

#### Teaching Tips:
- may have to troubleshoot pip install of flask (sudo tends to help fix)


#### Talking Points:
- have students save file from code along
- have them set global variable in terminal so Flask knows where their application code lives
- use this opportunity to explain global variables, and also why Flask needs one
- ```flask run``` and do any troubleshooting that comes up


-----
