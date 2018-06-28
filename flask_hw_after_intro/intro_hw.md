### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Part Time
 

# Flask: Intro Practice Problems

In this homework, you're going to write code for a few problems. We'll be building on older material like basic Python function writing and argument settings in functions.

You will practice these programming concepts we've covered in class:
* Writing a basic Flask app
* Changing the arguments of functions
* Writing functions and wrapping functions with decorators

------------

## Deliverables

For each of the challenges listed below, you will create a new `.py` file and write code to solve the problem. For example, you would create `problem1.py` with your solution code to the first problem. Run the file from the command line to check your work.

*Reminder: On your laptop, you can run the file from your command line with the following command:*

```
python problem1.py
```

> **Hint**: After finish writing your code, launch your server, go into your browser and be sure that your Flask app is outputting the intended data. 


## Requirements:

* By the end of this, you should have 2 different `.py` files (one for each problem). 

------------

# Homework Problems

## Problem 1: "Today your love, tomorrow the (hello) world"

### Skill You're Practicing: Writing basic Flask applications

Write a Flask app that returns your favorite food. 

#### Example Test Code
```
def giveFood():
    return "I could eat pepperoni pizza all day everyday."
```

#### Example Test Output
```
I could eat pepperoni pizza all day everyday.
```

**Hint 1:** 

Refer to your class notes for details about how to import the proper libraries and use the `if __name__ == '__main__'` pattern. 

**Hint 2:** 

Don't forget that you need to specify the URL's ending with our @app.route decorator.

```
@app.route("/")
```
Is our way of saying "at the homepage" 


----

## Problem 2: "All of de bugs!"

### Skill You're Practicing: Turning off debug mode

In production, we definitely do not want people to see a traceback if our code results in an error. 

Turn the debug mode off. 

#### Example Test Code
```
def hello():
    return "Ain't no bugs on me!"
```

#### Example Test Output
```
"Ain't no bugs on me!"
```

**Hint 1:** 

We're looking for an argument within `app.run()` that sets debug to `True`. We want to set this argument to `False`.

**Hint 2:** 

By default, Flask sets this argument to `False`.


