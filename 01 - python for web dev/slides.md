<!--
---
title: Python Basics: Intro to Python Web Dev
type: lesson
duration: “:60”
creator: Anna Zocher
Private gist location: #
Presentation URL: #
---
-->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python: Web Development
---

## Learning Objectives:
*After this lesson, you will be able to:*
* Use Python concepts covered in first three days of class
* Speak to how web developers use Python
* Describe what a web appliction and web frameworks are.

---
## Review

** review first x3 days - add after first 3 days done **
---
## Web Development with Python
#### What is Web Development?
- Web Devlopment: using programming to build websites that render in the users browser. 
- A website is a collection of code that can be categorized into two types: *frontend* and *backend*

# ![](https://images-cdn.9gag.com/photo/a8pzYPp_700b.jpg)
---
## Frontend vs Backend
* **Frontend** - everything we use that 1. renders in your browser, locally 2. styles and organizes our website
* **Backend** - operations happen on a server, information is then sent to the frontend
#![](https://vironit-bevc00m.netdna-ssl.com/wp-content/uploads/2016/08/front-end-vs-back-end-750x375.jpg)

----
## Client/Server Relationship
*How does our frontend (the actual page we see) of our website know what to display?*
*If we login to a website, how does it validate our information?*

* Websites talk to servers using a protocol we call **CLIENT/SERVER RELATIONSHIP**

#[](https://jmarkman.neocities.org/images/clientserver.png)
credit: jmarkman.neocities.org

---
## Client/Server Relationship
*How does it work?*
Video https://www.youtube.com/watch?v=7_LPdttKXPc
**embed video if possible**
---

## Client/Server Relationship Demo
Open website: [https://www.nypl.org/](https://www.nypl.org/)

---

## Client/Server Relationship Review
* Websites are collections of frontend code (HTML/CSS) and backend code (Python).
* Frontend styles and formats our webstie; backend provides the information and action
* Backend uses functions to guide actions and return data
* Client (your computer) sends a request to the Server; server returns information - loading the website

---
## POST vs GET

Client/Server interaction happens using HTTP protocol. 
* *HTTP* - the name of the protocol for how clients and servers interact. 
* *POST* - a request where information is being sent (for example when you submit a form with info)
* *GET* - when request is for something (for example: downloading a page of HTML from a server)
---
## HTTP
**HTTP**:
* stands for Hypertext Transfer Protocol
* HTTP is the language that the Client and Server speak to each other to communicate
* Originally used to request HTML from server, and then return to Client (thus the name!)

---
## POST vs GET
POST and GET are the two methods HTTP requests are made
* **POST:**
* Paramaters that are being sent are in the body of your web page (for example, in a form like when you login to a webpage)
* Used to update data or send data to the server
* Can make changes to the server

---
## GET
**GET:** 
* Default type of request method. 
* Used anytime the Client is asking the Server to just send something back, and no data is being sent to the server.
* We send these parameters in the URL (meaning that the url is where ther server looks for any GET info)
* Doesn't make any changes to the server

---
## Web Development with Python

### How and why do we use Python in web development?

---
## Web Development with Python
1. Python's built in **libraries** make it easy to use for a cross-discipline tasks
What do we mean? Python makes it easy to do a lot of data work through its built in libraries
It also makes it easy to display this data through its built in libraries
Few languages let you do both types of work so easily
2. Python's built **frameworks** make it easy to launch a web app. 
Django and Flask (what you are about to learn!) make it very "cheap" to launch a website.

---

## Recap
* Learned about Client/Server Relationship
* Learned about HTTP protocols and how web calls work!
* Learned about how and why we use Python for web development!

---
## Additional Resources
* [Fundamentals of Web Programming](http://interactivepython.org/runestone/static/webfundamentals/WWW/history.html)
* [Understanding the Difference Between Client/Server and P2P](https://www.techrepublic.com/article/understanding-the-differences-between-client-server-and-peer-to-peer-networks/)
* [Web Applications and the HTTP Protocol](https://www.youtube.com/watch?v=RsQ1tFLwldY)

