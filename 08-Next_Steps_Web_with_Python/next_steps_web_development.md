
-----


# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Next Steps in Web Development with Python
Kevin Coyle

-----

### Learning Objectives
*After this lesson, you will be able to:*
1. Identify common web concepts to dive into next
2. Identify common Python libraries used for front-end web development
3. Identify common Python based back-end web development tech stacks

---------

### I like this web development stuff, but where should I go next?
 <!-- Talking Points: 
 	We're going to go over 4 curated paths you could walk down --> 
- Extending Flask
- Front-End with Python 
- Back-End with Python 
- Other popular libraries for Python web framework

---

### Paths 
 <!-- Talking Points:    
 - There are multiple areas of web development open to you as Pythonista.
 - Since Python is both a: front-end and back-end language
 - You'have a wide array of options. 
 - What's this front-end/back-end distinction? TBH there's usually a bit of overlap and people are required to wear hats from one side or another, but generally:
   - front-end people handle the part of the website that people see
   - back-end people handle the server side - the part of where the site works, updates, and changes
 - Going down the front-end path is for you if you're one of those people who needs people to look just so.  
 - Going down the back end programming route would be for you if you didn't want to worry about how the site looks; you just want the programming challenges of getting the site online. Front end would be if you're more design inclined - you didn't want to worry about getting the website online, but just wanted to make a really cool looking site
  --> 
#### Path #1:
##### Front-end 

**Why** 
- You're designed inclined
- You want to make cool sites!
- You're using Python to accomplish the goal of propping up your designs,
**How** 
- Check out the section on Bootstrap below, as well languages like HTML, CSS, and JavaScript. 
- You can try modifying premade Bootstrap themes to get started!

#### Path #2
##### Back-end language
**Why** 
- You love programming
- You don't care as much about how the website looks
- You enjoy Python and the idea of using someone else's designs sounds great. 
**How**
- Check out the section on SQLAlchemy and PyMongo below, as well as servers like WSGI and NGINX
- You can try starting a MongoDB yourself and then having Flask retrieve data from there!
---

### Expanding on Flask
 <!-- Talking Points:    
 - Flask is fantastic web development framework.
 - Our first hello world app was ~ 7 lines of code. 
 - Flask has built the whole website for you - the front and back ends. But you can do each side individually, without Flask - people can write the front end using HTML and JS (maybe put "HTML and JS are done for you" as a subbullet under backend), and rely on your Python skills to host the site.
  - However, building modern websites with any framework (even one as lightweight as Flask) takes work.
 - Since we are primarily concerned here with Python and Flask, I'll give you a couple shortcuts, listed here on the slides. 
 - These integrate with Flask fairly easily. Yay!     --> 
- Bootstrap
- SQLAlchemy/PyMongo

---

### What is Bootstrap?
 
 <!-- Talking Points:   
 - Bootstrap was started by Mark Otto and Jacob Thorton at Twitter. 
 - One of the main use cases for Bootstrap is for people who like the idea of great looking websites, but don't like the idea of writing the CSS/HTML. 
 - Bootstrap can connect to Flask.        --> 
Bootstrap will handle all of the "pretty" stuff and Flask can handle most of the rest. 
Bootstrap can be easily handled by Flask with Flask-Bootstrap `pip install Flask-Bootstrap`

---

### How to get started with Bootstrap

- Install Flask-Bootstrap
- `git clone https://github.com/mbr/flask-bootstrap.git`
- `cd` into the flask-bootstrap directory. 
- run `pip install -r sample_app/requirements.txt` to install the required packages
- deploy Flask with Bootstrap by running `flask --app=sample_app dev`
- Go through directories. Comment out code to be certain you know exactly what every line is doing. 

Also:
https://getbootstrap.com/docs/3.3/getting-started/

---

### SQLAlchemy and PyMongo
 <!-- Talking Points:      
 - When we added data to our Flask app, we appended to a list. 
 - This is fantastic first start, but if you'd like to have a larger database, you'll need to look into databases like PostgreSQL, MySQL, or MongoDB.
 - Flask can integrate with a number of databases. 
 - Although there is no out-of-the-box with Flask, there are many libraries in Python.
 - Two that we'll highlight here are SQLAlchemy and MongoDB. 
 - There's an extension of Flask called Flask-SqlAlchemy `pip install Flask-SqlAlchemy` that allows you to connect to SQL databases using Python.
 - You might be asking yourself: what about these "NoSQL" databases I keep hearing about?
 - Remember how we "JSON-ified" our `return`? MongoDB is an open source database that stores JSON like "documents." 
 - Instead of rows like in Postgres and such, there can be any number, name, or heirarchy of fields.     --> 
You can install Flask SQLAlchemy with `pip install Flask-SqlAlchemy`
You can install Flask PyMongo with `pip install Flask-PyMongo` 
and just PyMongo with `python -m pip install pymongo`

---

### How to get started with PyMongo

First, install MongoDB:
- `brew update`
- `brew install mongodb`
- `brew install mongodb --devel`

Next, start your MongoDB:
- `mkdir -p /data/db`
- Note: if that results in an error, you need different priveleges. Run: `sudo mkdir -p /data/db`
- Start your database with the Mongo daemon with the command `mongod`

Then, add some data to your database using :

```
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'burritodb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/burritodb'

mongo = PyMongo(app)

@app.route('/burrito', methods=['GET'])
def get_all_burritos():
  burrito = mongo.db.burritos
  output = []
  for s in burrito.find():
    output.append({'ingredient' : s['ingredient'], 'burrito_necessity' : s['burrito_necessity']})
  return jsonify({'result' : output})

@app.route('/burrito/', methods=['GET'])
def get_one_burrito(ingredient):
  burrito = mongo.db.burritos
  s = burrito.find_one({'ingredient' : ingredient})
  if s:
    output = {'ingredient' : s['ingredient'], 'burrito_necessity' : s['burrito_necessity']}
  else:
    output = "No such ingredient"
  return jsonify({'result' : output})

@app.route('/burrito', methods=['POST'])
def add_burrito():
  burrito = mongo.db.burritos
  ingredient = request.json['ingredient']
  burrito_necessity = request.json['burrito_necessity']
  burrito_id = burrito.insert({'ingredient': ingredient, 'burrito_necessity': burrito_necessity})
  new_burrito = burrito.find_one({'_id': burrito_id })
  output = {'ingredient' : new_burrito['ingredient'], 'burrito_necessity' : new_burrito['burrito_necessity']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)

```
Save the above to a python file and then try making GET and POST requests!
---

### Web Frameworks that Aren't Flask
 <!-- Talking Points:    
 - You may of heard of some other Python based web frameworks like these listed on the board   
 - We're going to focus on the last two listed: Django and Pelican   --> 

- Pyramid
- Zope
- Bottle
- CherryPy
- **Django**
- **Pelican**

---

### What's Django?

 <!-- Talking Points:    
 - Django is similar to Flask in that it's a web framework. 
 - However, whereas Flask takes a "Lego-like" building blocks approach, Django comes with more of the bells and whistles built in.  
 - What's great about Django is that other developers have taken a lot of the hassle out of web development.
 - This includes some things that help developers out like these bullet points on the slide    --> 
- A complete, "batteries included" approach philosophy
- Security, like storing passwords as a hash, rather than directly storing them.
- Scalability, Django is highly scalable and many increbibly high trafficked websites like Disqus and Instagram

Installing Django can be done by following the installation guide on djangoproject.com 

---

### What's Pelican?
 <!-- Talking Points:      
- Recently, there's been a resurgence in popularity of static web pages.
- Blogs, and other sites that don't require as much updates to code are prime examples of sites that would use static webpages.
- Python has a library called Pelican which can generate these static sites for you (they generate all the HTML from a Markdown file that you create).    
- This means: you just write some python code, and all the HTML gets made for you! --> 
This is a really really really quick way to get a site up and running. 
`pip install pelican` 

---

### Web Development in General

 <!-- Talking Points:  
- We've covered some libraries as well as some places to go for front-end and back-end tech stacks. 
- However, we haven't even scratched the surface of web development as a whole. 
- The fine folks at Mozilla have put together a resource on learning web development which you can check out at developer.mozilla.org       --> 
[developer.mozilla.org/](https://developer.mozilla.org/)

---

### In Review: I want to...

#### Make a: Blog
IOW: I want to build simple, static websites in less than 10 minutes and then work on content.

I should look into...
- Pelican

#### Make a: Beautiful Website 
IOW: All this Python coding is a bit much for me.
I should look into...
- Front-end web dev
- HTML/CSS/Javascript

#### Make a: Beautiful Database 
IOW: All this Python coding is #goals.
I should look into...
- Back-end web dev
 - SQLAlchemy
 - MySQL
 - PostgreSQL
 - MongoDB

#### Make a: Awesomer version of a Flask based website
IOW: I really liked all the above and am right at home between front end and back end with Flask.
I should look into...
- More [Flask extensions](http://flask.pocoo.org/extensions/)

#### Make a: website but without all these libraries and extensions
IOW: I really the idea of this whole framework thing, but I wish there was only one, obvious way to do things.
I should look into...
- Django

---

## Review
We covered next steps with Flask, and web development with Python:
- Extending Flask
- Python front-end libraries
- Python back-end libraries for databases
- A few other Python based web frameworks

---

### Additional Reading
- [Explore Flask](http://exploreflask.com/en/latest/pym)
- [PyMongo Documentation](https://api.mongodb.com/python/current/)
- [SQLAlchemy's Fantastic Object Relational Mapper Tutorial](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html)
- [Django Documentation](https://docs.djangoproject.com/en/2.0/)
- [Pelican Documentation](http://docs.getpelican.com/en/stable/)