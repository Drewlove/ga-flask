# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Flask

---

## Learning Objectives:
*After this lesson, you will be able to:*
- Write your first, basic, Flask application!

---
## Basic Flask
#### What is Flask?
* Flask is a micro-web framework built using python
**What does this actually mean?**
---
## Basic Flask
#### History of Flask
* ~2010 a group of open source python developers release the first version of Flask!
* Before this: no easy way to use Python on the internet/for web apps!
* Flask is built using two libraries (already written bundles of code)
1. *Werkzeug* - a library to interface with the web. It helps to handle request and connections.
2. *Jinja* - a templating engine, which lets us write an html file once, and then apply that html file to all of our site

---
## Basic Flask
#### What is Flask?
* Flask uses both of these exiting libraries to create a basis from which we can easily build web apps!
* **[REVIEW]:** What is a web app? 
- a web app is a larger collection of code that uses the client-server relationship to render a website, and offers the user greater features then a static website. Likely these features will include some sort of data storage and retrieval as well.
* a web framework like Flask makes this all possible by providing the client-server relationship piece, as well as added features to make writing a larger web app easier
* a lot of webframeworks are even bigger then Flask (aka more features), or take more to setup - Flask is simple to use, easy to start using, and very flexible
* without Flask, or a web framework, we would have to write out everything of how to put our python app and run our python app on the internet.

---
## Real World Flask
* Pinterest - [www.pinterest.com](http://www.pinterest.com)
* Instagram Web Platform - [www.instagram.com](http://www.instagram.com)

**Why do both of these sites use Flask?**
- Both sites are high on user interactivity
- both have a large server load (lots of images to dowload, lots of actions on part of user)
- Flask makes is easy to:
    ** add new features quickly
    ** not have to worry about the actual connection piece of the website
    ** put all time sensitive work onto the server, and not on other parts of the website

---
<!-- can use either this repl or code in demo-code-basic folder -->
<iframe height=“400px” width=“100%” src=“https://repl.it/@AnnaZocher/introtoflask” scrolling=“no” frameborder=“no” allowtransparency=“true” allowfullscreen=“true” sandbox=“allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals”></iframe>

---
## Basic Flask

```import flask from Flask``` 
Flask is the name of the Class (group of code) we are using; flask is the name of the library. In programming we capitalize the names of Classes, and lowercase the names of libraries by convention. 

---
## Basic Flask

```app = Flask(__name__)``` 
We are telling our computer that we want to create a new intense of the Flask class, and name it app.

---
## Basic Flask

    @app.route(‘/‘)
    def index():
      return ‘Hello, World!’
**Comment out this code line by line to describe what is happening in our program.**

---
## Codealong
- follow as we build out Flask app we just walked through

---
## Running Flask App
- Flask (and lots of web frameworks) can be launched on the command line, giving developers more control and clarity into what is going on

1. Save basic Flask app as application.py
2. open terminal
-  *If Flask not downloaded, pip install flask*
3. set global variable (so flask knows where our main application logic lives)
*export FLASK_APP=application.py*
4. ```flask run```

---
## Recap
- Learned about Flask + web frameworks
- Wrote our first Flask app!
