# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Templates

#### Author: Kevin Coyle
-----

### Learning Objectives
*After this lesson, you will be able to:*
1. Explain what Jinja2 and why it's useful.
2. Successfully explain what a template design pattern in Flask does.
3. Create a template HTML document and pass variables into it via a Flask app.

---------

## Templates

Don't you hate it when you have to repeat yourself?

repeat yourself?

repeat yourself?

--- 

## DRY - Don't Repeat yourself
<!--  
- If it takes you 4 seconds to type out the code, you'd spend ~194 hours over the course of the next 20 hours just writing the code (4 seconds an hour * 24 hours * 365 days * 20 years). Ew! Not to mention the time to launch the shell, and even worse, all the sleep you'll lose, waking up once an hour to write that code. Sweet sweet sleep! 

- Better to write a program once that prints this for us. 

- This is part of what makes templating so powerful. 

- Rather than hardcoding all variables into our flask app, we can use a template to render some value (aka "data") that we assign to those variables, for us.

- Flask uses Jinja2 as its template engine.-->
Just to make a point? 

In programming, we try to follow a principle called DRY - Don't Repeat Yourself. 

To put this into perspective. Let's give an example with the following requirements:
Let's imagine a nightmare scenario where 
- The computer output some line of code like `print("hello world")` 
- This must happen every day, once an hour. 

One way to do this: 
1. Open a Python Shell in terminal, then write our code and execute it. 


----

## Jinja2

Underneath the hood, Flask is using a template engine called Jinja (aka Jinja2). Jinja is one of the most widely used template engines for Python.

Jinja is used in places that you might have visited already like: 
- Instagram 
- NPR.

---

## Why Jinja2? 
<!-- - Jinja2 is kind of like the engine that powers our vehicle (Flask). However, this happens under the hood. 
- We're peering under the hood real quick to get an idea of what our engine can do. 

Some examples of what makes Jinja2 awesome are: 
- Template Inheritance:
You can extend templates in very efficient ways.
- HTML Escaping
Malicious and naughty users can create XSS attacks by injecting HTML code into our site where other users insert data.
- Speed and Efficiency
Jinja2 is very fast. It compiles optimized Python code. 
- Flexible and Extensible
It's really easy to add our own filters and functions.-->

Jinja 2 has some really powerful features that web design folk want to take advantage of:

- Template Inheritance
- HTML Escaping
- Speed and Efficiency
- Flexible and Extensible

Why would we want to use it though? 
- Adding programming language to our HTML templates
- Transferring info from Flask to HTML
- Lets us separate data from how we present data to users

---
## Knowledge Check:

What's template inheritance?

<!-- Template inheritance is extending templates in very efficient ways -->

What's one reason why we might want to use templates, other than staying DRY?

<!-- Templates allow us to add programming languages to our HTML templates --> 

---

## Expanding on Hello World. 

We're about to create a Flask app with a template in it.

This will render a user's name. 

In doing this, we'll render a template that uses Python to display the value of a variable.

---
## Recreate `hello_world.py`

Open your text editor and type out the following.


```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello, World"

if __name__ == '__main__':
	app.run(debug=True)
```
Save this to a file named `hello_flask.py` 
---

## Deploy our hello_flask Flask script. 
<!-- After students launch this Flask app, lead them into the next concept by asking the following:
- This is all well and good, but what if we want to be able to dynamically add in some values or not put all of our content into the `return` of our function?

- This is where templates shine. Let's change our hello world Flask script a little. -->
- Open terminal 
- Launch `hello_flask.py` by typing `python hello_flask.py` then pressing the `Enter` key.
- In your favorite browser, head to `http://localhost:5000`
---

## Adding Templates
<!-- This is the function that Flask uses to... you guessed it: render our template(s)!
For this exercise, we want to add some programming language (Python) into our HTML template.-->
First, we'll import `render_template` 

```
from flask import Flask, render_template 
```
This is the function that Flask uses to... you guessed it: render our template(s)!

---

## Our directory tree
<!-- Next, we'll create a folder and an html file. 

> Our render_template is going look for a template folder.

After we make our template folder in our project and add in our html template, our directory will look like the tree print on the screen
-- >
```
project
│   
│
└───app
│   │   hello_flask.py
│   │   
│   │
│   └───templates
│       │   hello.html
```
Go ahead and create a folder called "templates" and in your text editor, create a new file called `hello.html`

---

## Create our HTML template
<!-- - Now edit `hello.html` 
- This is some fairly basic html. 
- We're going to use some templating to pass in variables. -->
Now edit `hello.html`. 

```
<!doctype html>
<html>
   <body>
   
      <h1>Hello {{ name }}!</h1>
      
   </body>
</html>
```

---

## Templating Syntax with Jinja
<!-- - What's awesome about this, is that inside of these brackets, we can pass in Python syntax. 
- In our example, we have a variable, which we're calling `name`. 
- Whatever we assign to the variable `name` will be rendered when our page renders. 
- Statements are where we would pass in logic like {%if this thing%} {% else that thing%}-->
1. In Jinja, templates are rendered with double curly brackets like `{{ }}`
- Use case here is our variable example above
2. Statements are rendered with curly brackets and percent signs like `{% %}`
- A use case here is passing in logic like 
```
{% if name == 'kevin' %}
# Do the thing
{% else %}
# Do all the other things
```

---

## Rendering a template in Flask
<!-- We're going to modify the rest of our Flask app to pass some values into our variable in the template (curly brackets). Let's change the rest of our hello_flask.py so that the whole thing looks the following script on screen.

Here, we use `render_template` function which takes in two arguments: 
1. Our template name, `hello.html`, 
2. Our **context** which, from the documentation is "the variables that should be available in the context of the template." 

Here, our variable is name which is passed into the <user> part of our route, and then becomes the value that we assign to the variable called `name`. -- >
Let's change the rest of our `hello_flask.py`:

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello, World"

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name=user)

if __name__ == '__main__':
	app.run(debug=True)
```
---

## Seeing our Flask App in Action 
<!-- -Note: if you want to change the name in your browser, just change the url where "kevin" is, like: localhost:5000/home/[some Pythonista's name here]

Teaching points:
- Open terminal and from the command line, launch `hello_flask.py` by typing `python hello_flask.py` 
- Then press the `Enter` key. 
- Then, in your favorite browser, head to `http://localhost:5000`
- Notice our homepage is still the same. 
- Next head to http://localhost:5000/hello/kevin
--> 
- Open terminal and from the command line, 
- launch `hello_flask.py` by typing `python hello_flask.py` then pressing the `Enter` key. 
- Then, in your favorite browser, head to `http://localhost:5000`
- Notice our homepage is still the same. 
- Next head to http://localhost:5000/hello/kevin

And hello back to you, you awesome Pythonista you!

---
## Knowledge check:

What two arguments did we pass into the `render_template` function?
<!-- "home.html" - our template name; and name, which is our context -->

What's one reason we use templates?
<!-- - Adding programming language to our HTML templates
- Transferring info from Flask to HTML
- Lets us separate data from how we present data to users --> 

--- 
## Your Turn!

<!-- Now it's your turn. See if you can create a web app that uses a template with an if/else statement within to display "hello kevin" if the route name ends in kevin, else something else if the route name is a different name -->
Deliverables: 
- Modify our HTML file from above
- Include if/else logic to render one name if our route ends in that name, else render something else
- Launch your Flask app and check the results	

---

## Review:

- We just learned what Jinja templating engine is, what it does, and why we use templates.  
- We learned how to use templates with Flask.
- We created an HTML document that has a template in.   
