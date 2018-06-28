
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) APIs and Requests in Flask

Authors: Kevin Coyle and Dave Yerrington
---

## Learning Objectives
*After this lesson, you will be able to:*
1. Explain what an API is, and learn how to create one
2. Create an API that makes a GET request with Flask
3. Create an API that makes a POST request with Flask

---

# APIs 
<!-- -In your internet browser, head to (the link on the slide)

- That's some awesome data on Chewbacca. 
- But let's view that in Chewbacca's native tongue. 

Now head to (the second link on the slides)

- This is the same data in Wookie :) -->

In your internet browser, head to [https://swapi.co/api/people/13/?format=json](https://swapi.co/api/people/13/?format=json)

Then...

head to [https://swapi.co/api/people/13/?format=wookiee](https://swapi.co/api/people/13/?format=wookiee)

---
## Recapping
<!-- 
- At a theoretical level, you can think of interfaces kind of analogous to real world counterparts:

- Door handles. These interfaces get pushed or pulled, and the door opens to a new space. We could even have crazy DeLorean style doors that open upward.
- A standard telephone. When you call someone, you are connected from your space to another space using this interface.-->

- Application Programming Interfaces (APIs) are a set of routines, protocols, and tools for building software applications. 

- APIs specify how software components should interact. 

Examples:
- Door handles. 
- A standard telephone. 

----

## Knowledge Check

What's the difference between calling and creating an API?
<!-- Calling an API allows you to retrieve data, while creating an API makes some data that you want to publish accessible -->

---
### Web APIs. 
<!-- 
  - Today, we'll write a function based on displaying a list of heroes of the Python/programming world.
- Using the abstracted examples from a second ago, you can think of the function call as the phone number that you're dialing, or the handle that you make a request on. 
- Many web programmers today use web APIs. The rise of Javascript and the current state of programming techniques are the principal movers of this rise. We're going to create an API today using Flask.
- Because of how interactive many websites have become (again, fingers pointed at Javascript), many other languages like Python started co-opting standards to communicate data to and from servers. -->
A web API is a list of function calls that are made to remote servers.

The function call is sent by encoding a URL (an HTTP request). 

- Many web programmers today use web APIs. 
- We're going to create an API today using Flask.

---
### HTTP
<!-- 
There are **clients** that _make_ the requests and **servers** that _receive_ those requests. 

- HTTP clients respond to HTTP responses from a web server/HTTP server.  
- Web servers receive HTTP requests and generate HTTP responses. -->
HyperText Transfer Protocol is:
1. A system of rules (the "Protocol" part) 
2. That determines how web pages (the "HyperText" part),
3. Get sent from one place to another (the "Transfer" part). 

- **Clients** 
- **Servers** 

---

### CRUD
<!-- 
- CRUD operations are the four basic functions in persistent storage. 
- CRUD operations are everywhere in programming
- Here, we're most concerned with how our API is going to Create, Read, and Update data via an HTTP url --> 
- *C* Create
- *R* Read
- *U* Update
- *D* Delete

---

### HTTP Requests
<!--here are HTTP methods to map to CRUD (create, read, update, delete) operations to HTTP requests:
-->

- GET
	- **R**eads information. GET requests must be safe and idempotent (regardless of how many times it repeats with the same parameters, the results are the same).
- POST
	- Requests that the resource do something. Usually this used to **C**reate something, but it can also be an *U*pdate.
- PUT
	- Stores an entity. PUT can *C*reate or *U*pdate an existing one. PUT requests are idempotent. Idempotency is the main expectation difference in PUT from POST. 
- PATCH
	-**U**pdates the specified fields of an entity. PATCH requests are idempotent. 
- DELETE
	- Request that a resource be removed or **D**eleted. Note that this doesn't necessarily have to happen immediately.

---

#### Knowledge Check:
What does the acronym CRUD stand for?

<!-- Create, Read/Retrieve, Update, Delete/Destroy -->

---

### Creating an API with Flask
<!-- - Please open your text editor of choice, a browser, and Terminal.  

We're going to create an example of an APIs that:
- Takes in a list of dictionaries
- Parses that list based on what we pass into the API 
- Returns a JSON with the appropriate data.
--> 
Now we will make a RESTful API using vanilla Flask.

---
### JSON
<!-- The most that we need to know right now about JSON:
- JSON has a similar data structure in Python: the dictionary


We're going to modify `hello_api.py` again in your code editor--> 
- Both Dictionaries and JSONs have key/value pairs
- Both Dictionaries and JSONs are wrapped in curly brackets `{}`

---
### Basic App


Type our our Hello World app. 
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello, World"

if __name__ == '__main__':
	app.run(debug=True)
```
- Which we can save to a file called `hello_api.py` 
- And we can deploy this app from Terminal using `python hello_api.py`



---
### New Functions 
We're going to import 2 new functions. 

Modify the first line to include `jsonify` and `request`

```
from flask import Flask, jsonify, request
```

---

### First API route
<!-- - Let's add a new route under our hello world homepage.
- Save your python file. If we have our code right, our new page should return our JSON!
Open your browser and first head to `localhost:5000`

Then head to `localhost:5000/api` 

It worked! Congratulations! -->
Let's add a new route under our hello world homepage.

```
@app.route('/api', methods=['GET'])
def returnJsonTest():
    return jsonify({'What happened?': 'It worked!'})
```

`localhost:5000`

 `localhost:5000/api` 

---

### Altering data with APIs
<!-- - This is cool, but what if we want that data to change?
- Let's create a list like the one on the screen
- Let's add that into our script in hello_api.py
- The full script looks like the second block of code --> 

```
heroes = [{'person': 'Peter_Norvig'}, {'person': 'Gilbert_Strang'}, {'person': 'Ada_Lovelace'}, {'person': 'Guido_van_Rossum'}] 
```


```
from flask import Flask, jsonify, request 

app = Flask(__name__)

heroes = [{'person': 'Peter_Norvig'}, {'person': 'Gilbert_Strang'}, {'person': 'Ada_Lovelace'}, {'person': 'Guido_van_Rossum'}] 

@app.route('/')
def hello():
	return "Hello, World"

@app.route('/api', methods=['GET'])
def returnJsonTest():
    return jsonify({'What happened?': 'It worked!'})

if __name__ == '__main__':
	app.run(debug=True)
```
---

## Knowledge Check:

What two new functions did we add into our import?

<!-- jsonify, request -->

---

### APIs to return all data 
<!-- - We also need to add in some code to give us the data from our list.
- We'll add a function to return all teh dataz.
- Type out the code on the slide in your hello_api.py script, below the `def -->

```
@app.route('/heroes', methods=['GET'])
def gimmeAllHeroes():
    return jsonify({'heroes': heroes})
```
---

### APIs to return some data
<!-- There's a few things going on here:
- We loop over our list of heroes
- We return one of the heroes if our name in the HTTP address matches the name in our function. -->
```
@app.route('/heroes/<string:name>', methods=['GET'])
def gimmeOneHero(name):
    names = [hero for hero in heroes if hero['person'] == name]
    return jsonify({'hero': names[0]})
```
---

### Creating a POST rquest with flask 
<!-- - Let's try adding data to our list of heroes with a POST request. Right now, our app looks like the following on the screen -->

```
from flask import Flask, jsonify, request 

app = Flask(__name__)

heroes = [{'person': 'Peter_Norvig'}, {'person': 'Gilbert_Strang'}, {'person': 'Ada_Lovelace'}, {'person': 'Guido_van_Rossum'}] 

@app.route('/')
def hello():
	return "Hello, World"

@app.route('/api', methods=['GET'])
def returnAll():
    return jsonify({'message': 'Okay I get it!'})

@app.route('/heroes', methods=['GET'])
def gimmeAllHeroes():
    return jsonify({'heroes': heroes})

@app.route('/heroes/<string:name>', methods=['GET'])
def weNeedAHero(name):
    names = [hero for hero in heroes if hero['person'] == name]
    return jsonify({'hero': names[0]})

if __name__ == '__main__':
	app.run(debug=True)
```

---

### Adding our new POST function 
<!-- - We'll use the same route, and if POST request gets made, we'll append that into our heroes list.
- Add in the following function that I've named `addMyHero`-->

```
@app.route('/heroes', methods=['POST'])
def addMyHero():
    newhero = {"person": request.get_json()["person"]}

    heroes.append(newhero)
    return jsonify({"heroes": heroes})
```

---

### Knowledge check

Assuming our code doesn't have any errors, what should happen when our POST request takes place?
<!-- We should append a hero (our data) into our heroes list (our database) -->

---

### Profit 

<!-- 
- Now we'll check to see if our POST request works. 
1. Open a new terminal window, and `python hello_api.py`
- This will launch our server
2. Once your Flask app has started, open a new tab (Command + T)
We need the server to remain running locally. 
3. In the new tab, we're going to make a POST request with a particular content type of JSON
- The content type here is JSON, but we could extend this to be other data types by changing our function and then changing the curl command we run below 
4. Type `curl -X POST -H "Content-Type: application/json" -d '{"person":"<<insert a name here>>"}' http://localhost:5000/heroes`
- cURL is a command line tool. It stands for Client URL. The high level, hand-wavey description is that it is like a browser, but in your command line. More formally, it's a command line tool for getting or sending files with URL syntax. 
5. We should see our new hero list with our personal hero appended! -->

Now we'll check to see if our POST request works. 

1. Open a new terminal window, and `python hello_api.py`
2. Once your Flask app has started, open a new tab (Command + T)
3. Type `curl -X POST -H "Content-Type: application/json" -d '{"person":"<<insert a name here>>"}' http://localhost:5000/heroes`
5. We should see our new hero list with our personal hero appended!

---

### Knowledge Check

What's the difference between a POST and GET request?

<!-- A POST request will Create or Update something, while a GET request will Read something -->

---

### Quiz
<!-- despite what the variables, and key/value pairs are named, the correct answer is letter A-->
Which of these is the right code for a POST request:

#### A.
```
@app.route('/myapiroute', methods=['POST'])
def butAmIMakingARequest():
    type_of_request = {"requestType:" :" This is definitely a GET Request"}
    requestage.append(type_of_request)
    return jsonify({"theAnswer" :  requestage})
```
#### B. 
```
type_of_request = [{"requestType:" :" This is definitely a POST Request"}]
@app.route('/myapiroute', methods=['GET'])
def butAmIMakingARequest():    
    return jsonify({"theAnswer" :  type_of_request})
```    
___

## Review
We covered APIs and Request in Flask:
1. What an API is.
2. How to create an API that makes a GET request with Flask
3. How to create an API that makes a POST request with Flask

---

### Additional Reading
- [Flask JSONify Documentation](http://flask.pocoo.org/docs/1.0/api/#flask.json.jsonify)