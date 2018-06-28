
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Variables and Routing in Flask
Kevin Coyle

-----

### Learning Objectives
*After this lesson, you will be able to:*
1. Create a variable/value in Flask app and display the value on a webpage
2. Read in a variable/value from outside of Flask app
3. Create a route in Flask

-----

### Python as OOP
<!-- 
	- One of the things that makes python so fantastic is that it is object oriented. 
	- Assigning variables turns them into a type of object
	- with the object, we can do some awesome things
	- We're going to look at variables in our flask app. Creating variables allows us to return values of those variables, as well as providing us with all the methods and attributes in that type of object.
	- Routes allow us to extend this a step further - we can take variables and put them into our URL, which we can then use to render some data on the page.
-->
- Why variables?
- Why routes?

------

## Variables and Routing in Flask

There are two parts to this lesson. 
1. The first half is concerned with Variables in Flask
2. The second half is concerned with Routing in Flask. 

## Part 1. Variables.
---

### Variables in Flask vs. Python Variables
 <!-- 
 	- When we are talking about variables here, we are talking about the same thing as variables in base Python
 	- You assign a variable to a value and that value gets stored in memory.
 	- We'll go over some common use cases for including variables in your flask app 
 	- Note though that using variables in templates and requests will be covered in a later lesson. -->

`x = "this string"`

Use cases:
- In routes 
- In templates
- In requests

---

### Ways to read in a Variable

<!-- 
	- There are several ways to obtain the value for a variable. 
	- Depending on that value and what it represents, there are different ways of going about entering that into our flask app
	- The first is to have the variable assignment take place right in our flask app. 
	- Another is to read it from a Python script, like you would for any other library
	- Yet another is to read it in from a file, unlike you would import any library. 
	-->

Variables come from:
1. Within our Flask app
2. From another Python file
3. From any other file

---

### Reading directly from our Flask app
<!--
- The easiest way to obtain a value from a variable in flask is to assign it directly in your flask app.
- This makes sense if we are only trying output a very very small amount of information. 
- Consider the following modification on our hello world app
-->

`hello_variables.py`

```
from flask import Flask

app = Flask(__name__)

my_job_title = "rockstar Pythonista"

@app.route('/')
def hello():
	return "Hello, " + my_job_title

if __name__ == '__main__':
	app.run(debug=True)
```
---

### Reading from a Python file

<!-- 
	- The next way to read in a variable is to assign it in a Python file, then import that file 
	- This is considered the most "pythonic" way to read variables into other Python files. 
	- A great use case for this is when you'd like to have your secret info (tokens, passwords, etc.) in a file that isn't your Flask app
	- When you push your code to GitHub, you can then have your flask app out for the world to see, and your passwords safely in a file on your local drive
	- Another use case is file management. Pretend you have a lot of variables which may not make it into every file, but you want a "master file" to read all these variables from. 
	- In order to use this approach, you need another file that ends in ".py" 
	- You then read this file into your flask app with an "import <myFile>"
-->

Other Python File "mySecrets.py"

```
username = "Guy Fieri"
password = "flavortown"
```

Flask App "hello_variables.py"

```
from flask import Flask
import mySecrets

app = Flask(__name__)

my_name = mySecrets.username
my_password = mySecrets.password

@app.route('/')
def hello():
	return "Hello, " + my_name + ", welcome to " + my_password

if __name__ == '__main__':
	app.run(debug=True)
```

--- 

### Your turn

Now it's your turn! 

- Make a file called `theVariables.py`
- Insert some variables into that file
- Import theVariables into your Flask app
- Use the values from theVariables in your Flask app.

---
### Reading from a non-Python file 

<!-- 
	- Yet another way to read variables in is in non-python files. 
	- Not all data/info you'll need will be in a static python file
	- This approach is a combo of one of the earlier two approaches
	- Pretend say you have another file that's a .txt file 
	- We can do two things:
	 - read that txt file in directly in our flask app and set that to a variable (like approach 1)
	 or
	 - read that txt in with another file and save that to a variable which your Flask app reads (like approach 2)
	 - here, we take approach #1. first though we create a txt file
	 - then we open it with os and file open
	 - then we set that txt to a variable and print that variable in our route function
-->

Let's create a `.txt` file called "hi.txt" in the same folder where our app lives. We'll include some poetry from Shakespeare.
```
So are you to my thoughts as food to life,
Or as sweet-seasoned showers are to the ground;
```

Then we'll add a bit in our Flask app:
```
import os
file_path = '.'
with open(os.path.join(file_path, 'hi.txt')) as f:
    the_text = f.read()

@app.route('/text')
def read_txt():
	return the_text

```

---

### Knowledge Check

What were the three approaches to read in variables that we discussed?

<!-- reading directly in our flask app, reading from a python file and importing, and reading from a non-python file -->

----

## Part 2. Routing.

---

### What is that "@app.route('/')" anyways?
<!-- 
	- By now, you may be wondering about that `@app` that we keep putting on the line before our function
	- @ is a way to use a "decorator"
	- a decorator is a way to put a python function into another python function.
	- More formally, this process is called "Wrapping a function" inside of another function
	- You can check out more on decorators later, but for now, knowing that our @app.route(endpoint) is a way that we pass an argument - the endpoint- into a routing function
	- IOW: we tell our Flask app to listen to a particular endpoint and then we have a function that happens if that endpoint gets hit
	-->

```
@app.route('/sayHi')
def hello():
	return "Hello, Mr. Fieri."
```
 
---

### What is a route?


<!-- 
	- A route in our context here consists of our localhost:5000, as well as the rest of our URL.
	- We pass the rest our our endpoint into our app.route function as an argument
	- This means everything inside of the parentehese and inside of quotes become our URL
-->

http://localhost:5000/sayHi
---
### Variables in the route

<!--
	- Okay so I said these are two separate concepts, but that's only halfway true.
	- We can actually assign values in the URL to into variables in our Flask app
	- Why would we do this? Because we can change the URL to reflect what sort of data we wish to see
	- In the code snippet you see here: we are assigning the name variable to a value, which we insert into our function and then return to the user, in the middle of a sentence
-->

Let's add in a new route:
```
@app.route('sayhi/<name>')
def hello(name):
	return "Hello, " + name + ", your coding skills impress me!"

```
http://localhost:5000/sayHi/guy
---

### Your turn!

Try modifying the functions in our Flask app to display the following values:
1. An integer, given that integer is in our route
2. The product of an integer in the route multiplied by 4
3. A string passed into the URL, then displayed four times in a row. 

---


## Review
We covered Variables and Routing in Flask:
1. We created a variable/value in Flask app and displayed the value on a webpage
2. Read in a variable/value from outside of Flask app
3. Created a route in Flask

---

