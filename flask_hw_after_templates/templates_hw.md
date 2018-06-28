### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Part Time
 

# Flask: Templates Practice Problems

In this homework, you're going to write code for a few problems. 

You will practice these programming concepts we've covered in class:
* Variables
* Routing
* Templates

------------

## Deliverables

For each of the challenges listed below, you will create a new `.py` file and write code to solve the problem. For example, you would create `problem1.py` with your solution code to the first problem. Run the file from the command line to check your work.

*Reminder: On your laptop, you can run the file from your command line with the following command:*

```
python problem1.py
```

> **Hint**: After finish writing your code, launch your server, go into your browser and be sure that your Flask app is outputting the intended data. 


## Requirements:

* By the end of this, you should have 4 different `.py` files (three for the first problem, and one for the second problem). 

------------

# Homework Problems

## Problem 1: "Variables vary very for weary Vikings"

### Skill You're Practicing: Passing variables into your Flask app

Write a Flask app that reads in a variable from another file whose value is your favorite food. 

For this problem, you'll have 3 slightly different versions. 
1. The first version will use a variable in your Flask app.
2. The second version will read a variable in from a Python file.
3. The third version will read a variable in from a `.txt` file.

#### Example Test Code
```
favorite_food = Chicken
favorite_dish = BBQ Chicken Pizza
```

#### Example Test Output
```
"My favorite food is chicken on top of my favorite dish, BBQ Chicken Pizza"
```

**Hint 1:** 

Refer to your class notes from the variable lesson for how to read in a variable in each approach/style.

----

## Problem 2: "Routing"

### Skill You're Practicing: Creating routes with Flask

Make a copy of one of the three Python files from problem #1. We're going to modify it.

Create a route whose endpoint is a variable. Pass that variable into your Flask app. 

#### Example Test Code
```
http://localhost:5000/<food>
```

#### Example Test Output
```
We all know that chicken is not only good, it's good for you. 
```

***Hint 1:**** 

Recall that we need to put an argument into our function that gets wrapped by the @app.route.

---

## Problem 2: "Good artists copy"

### Skill You're Practicing: Using templates to render Python

Make an html file like the one from our lesson on Templates.

Modify the content of the HTML file. 

Create a flask app that renders this template. Include a variable that you pass into the template.

#### Example Test Code
```
render_template('index.html', name=user)
```

#### Example Test Output
```
"Hi there Akilah. It's great to see you today!"
```

**Hint 1:** 

Remember: templates for variables use the double brackets `{{}}`

**Hint 2:**

Our module to use is `render_template`




