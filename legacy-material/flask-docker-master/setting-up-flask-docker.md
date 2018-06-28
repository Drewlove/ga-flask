<img src="https://snag.gy/seOJAm.jpg">

> <img src="https://snag.gy/aAmMW0.jpg" align="left" style="float: left; width: 200px;" width="150"> **Docker Update** <Br>We've recently updated this article for students using the Docker environment.  There are references for using the `pip` package management tool, which you can safely ignore if you are using Docker because we will be building a container that will automatically install the required packages from the beginning.  So if you're using Docker, take note of the specific setup instructions, and ignore anything related to `pip` or `virtualenv`.

This is work in progress that seeks to convey the basic procedure for creating a minimum web service which could possibly:

 - Serve data
 - Update a machine learning model
 - Get predictions from a model
 - Build a minimal dynamic website

So what this guide aims to do is guide you through the bare minimum steps to setup a "Flask" application.

## Docker Setup

If you are using docker, we will be cloning a repository that contains a `Dockerfile`, a `requirements.txt`.  We will be clone a repo with all of these assets in it, then using Docker to provision our Flask container.

### 1. Create a flask-apps directory in your home directory

```
mkdir ~/flask-apps
```

### 2. Clone Flask Docker Repo

Go into your flask-apps directory, then clone our `flask-docker`.

```
cd ~/flask-apps
git clone https://git.generalassemb.ly/dsi-plus-2/flask-docker
```

### 3.  Build Docker Image

```bash
cd flask-docker
docker build --rm -t flask-dsi-plus .
```
![](https://snag.gy/O3vIEs.jpg)

### 4.  Run Flask
```bash
docker run -it -p 5000:5000 -v `pwd`:/src --rm flask-dsi-plus
```
> This will load the `service.py` file as the Flask application.  If you want to use a different file, you can rebuild the Docker image to change the Python file that's loaded:
> `docker build --build-arg SERVICE_FILE=some_other_file_here.py --rm -t flask-dsi-plus .`

### 5. Load your web application
> These routes will not exist until we create them later.  If you've gotten this far, great, just hang tight and we will build up to this point later in the codealong.

After running the application with Docker, you should be able to see your application endpoints here:

* http://127.0.0.1:5000/
* http://127.0.0.1:5000/json-test
* http://127.0.0.1:5000/predict-student

OR if you are running Flask on an EC2 instance visit http://**YOUR-PUBLIC-IP:5000** instead. If you are have connectivity problems ensure that port 5000 is open in your security group.

---
# <img src="https://snag.gy/8Gens5.jpg" style="float: left;" width="150">Non-Docker Setup
## 1. Setup a project directory space - (not using Docker)

>  Optionally, you should consider updating or installing the latest version of virtualenv.  So far we've been working with "conda" environments.  Virtualenv is an alternative to conda environments that help you work with isolated Python environments.  This is useful when you want to deploy an application into a production environment where it is available 24/7, with minimal operating libraries.  Would you want to make it a requirement to deploy all libraries we use in class to a production environment in order for an app with very simple features to run?  It can be complicated to manage Python library dependencies that may even work differently on OSX than say a Linux environment.  Application library dependencies are something you want to keep to an absolute minimum while operating in production.
>
> #### Upgrade / install Virtualenv
> `conda install virtualenv`

First, we should setup a new directory in our home directory called _"~/virtualenvs"_, then create a virtualenv called "flaskservice".

```
mkdir ~/virtualenvs
cd ~/virtualenvs
virtualenv flaskservice
```

This will create a new virtual environment structure in a new directory called "~/virtualenvs/flaskservice".

**The output should looks like this**
![](https://snag.gy/AdKY9m.jpg)




> We will walk through in class re: "What is a virtualenv and how is it different than conda?"

#### 2. Activate virtualenv "flaskservice" - (not using Docker)

Where in conda we "source activate dsi", with virutalenvs, we need to be in the base directory of the virtualenv of interest, then type:
```
. bin/activate
```

So literally, after you create "flaskservice" virtualenv, we will change into that directory, and activate our new environment.

```
cd ~/virtualenvs/flaskservice
. bin/activate
```

We should see a bash prompt denoting our **activated** virutalenv.

![](https://snag.gy/WjNCvM.jpg)

> We can deactivate our virutalenv by simply typing `deactivate`

#### 3. Install packages - (not using Docker)

This is a fresh virutalenv so we need to install some packages to make use of anything so we will be using the following packages:

```
pip install Flask pandas scikit-learn scipy
```
> Make sure you have "activated" your virtualenv before doing this.

#### 4. Create a new Python file called "service.py" - (not using Docker)

Add these contents:

```python
from flask import Flask, jsonify, request
from sklearn.linear_model import LogisticRegression
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

This will setup a very barebones application.

#### 5. Setup environmental variable and run your service - (not using Docker)

```bash
export FLASK_APP=service.py
export FLASK_DEBUG=1
flask run
```
The output of your console should look similar to this:
```bash
(flaskservice) Davids-MacBook-Pro-4:flaskservice davidyerrington$ flask run
 * Serving Flask app "service"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Your service is now accessible locally through your web browser:

http://127.0.0.1:5000/

> To quit your service, you simply type **ctrl-c**
> Also, because we use `export FLASK_DEBUG=1`, the service will automatically reload whenever we save our file.  Neat!  This will save lots of time.

#### 6. Setup a new "json" route - (not using Docker)

Add a new method with decorator to our **service.py** file

```
@app.route('/json-test')
def json_test():

    my_data = [
        {"student": "Anthony", "Speed": 23.5, "Power": "over 9000"},
        {"student": "Ruairi", "Speed": 23.55, "Power": "over 9000"},
        {"student": "Sam", "Speed": 23.2255, "Power": "over 9000"},
        {"student": "Evan", "Speed": 23.52553234, "Power": "over 9000"},
    ]

    return jsonify(my_data)

```

Then check it out in your browser:
http://127.0.0.1:5000/json-test

Also, let's load up a Jupyter notebook session and see if we can load it into a dataframe:

```
import pandas as pd

df = pd.read_json("http://127.0.0.1:5000/json-test")

```
**Can you get this to work?**

#### 7. Build a basic predictive model and serve the predictions

Below is a function that will build a predictive model each and every time with test data, then look for the parameter "speed", and serve a response with the predicted class labels, and associated probabilities for each class.

```python
@app.route('/predict-student')
def predict_student():

    my_data = [
        {"student": "Anthony", "Speed": 23.5, "Power": "over 9000"},
        {"student": "Ruairi", "Speed": 23.55, "Power": "over 9000"},
        {"student": "Sam", "Speed": 23.2255, "Power": "over 9000"},
        {"student": "Evan", "Speed": 23.52553234, "Power": "over 9000"},
    ]

    df = pd.DataFrame(my_data)

    logreg = LogisticRegression()
    model = logreg.fit(df[['Speed']].values, df["student"].values)
    speed = request.args.get("speed")

    if speed:
        predicted = model.predict([float(speed)]).tolist()
        probabilities = model.predict_proba([float(speed)]).tolist()
        result = {
            "response": "ok",
            "predictions": predicted,
            "probabilities": {student: probabilities[0][index] for index, student in enumerate(model.classes_.tolist())}
        }
    else:
        result = {"response": "not found", "message": "Please provide a model paramter to predict!"}



    return jsonify(result)
```

To see how this works, load this endpoint and experiment with the parameter "speed":
- Values between 1-30
- No value set
- String type value (see the error)

---
### End non-Docker Setup
---

# Practice

Build an endpoint called "predict-iris" that will use a classification method of your choice.

1. Build a response that will react to these parameters:
- sepal_len and sepal_width
- Have the response return a message that includes class predictions and probabilities (if the model provides)
- Have the response return a message to inform your users to set the correct parameters if they are not set

2. Extend your model to include the additional 2 paramters
3. Extend your service to accept multiple predictions at once
> Check this out for handling multiple input items: http://stackoverflow.com/questions/14188451/get-multiple-request-params-of-the-same-name

**BONUS**
4. Build in cross-validation and additionally return the recall, precision, for each prediction.
5. Save a static copy of your model (ie: from a notebook), then load it once in the beginning of your service.py app.  Refer to it in your route method so you don't have to fit it every time.

See these details:
http://scikit-learn.org/stable/modules/model_persistence.html
http://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/

Here is some reference / starter code to get you going with the dataset:
```python
from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
df = pd.DataFrame(data['data'], columns=['sepal_len', 'sepal_width', 'petal_lengh', 'petal_width'])
```

### Conclusion

For a more complete tutorial / deep dive on a slightly more "web app" type application, check out the main flask walkthrough on their site.  It's quite good.  In the future we will learn to build a much more in-depth web application using Django.

http://flask.pocoo.org/docs/0.12/tutorial/

## Putting Together a Front-End

Let's make a more user-friendly model deployment. Instead of taking arguments via the HTTP request and returning results in the form of JSON, we are going to write a (rudimentary) front-end interface.

#### 1. Ready the project directory
Make a `templates` folder inside of your Flask project directory. Then `touch` an empty file called `base.html`.

#### 2. Fill out a minimal html page with a submission form
Using your text editor add this html code to `base.html`:
```
<html>
<head>
  <title>Predict the runner!</title>
</head>

<body>

  <h1>Make a prediction!</h1>
  <form action="/predict-student-interface" method="POST">
  Speed:
  <input type="text" name="speed" required>
  <button type="submit">Submit</button>

  </form>

{% if output %}
<b>Predicted Class:</b> {{ output }}
{% endif %}

</body>
</html>
```
Notice the content in curly brackets `{% if output %}` .. `{% endif %}`. This is the Jinja templating language, not HTML. It dictates how information flows from the Flask backend to be rendered in the template.

##### 3. Modify the `service.py` Backend

Instead of always returning JSON, we want our view to return the base HTML template to collect predictor information from the forms, then render the model's prediction onto the page after it has been submitted.

Key modifications to for a frontend:
* add `from flask import render_template` to the imports
* Only return the predictions if `request.method == "POST"`
* Return the rendered template with output predictions instead of JSON

**Final code**
```
@app.route('/predict-student-interface', methods = ["GET", "POST"])
def predict_student_interface():

    my_data = [
        {"student": "Anthony", "Speed": 23.5, "Power": "over 9000"},
        {"student": "Ruairi", "Speed": 23.55, "Power": "over 9000"},
        {"student": "Sam", "Speed": 23.2255, "Power": "over 9000"},
        {"student": "Evan", "Speed": 23.52553234, "Power": "over 9000"},
    ]

    df = pd.DataFrame(my_data)

    logreg = LogisticRegression()
    model = logreg.fit(df[['Speed']].values, df["student"].values)

    output = None

    if request.method == "POST":
        speed = float(request.form["speed"])
        output = model.predict(speed)[0]

    return render_template("base.html", output = output)
```


## Extensions
* Make an input front-end for the Setosa model
* Pickle the setosa model so you don't need to re-train it every single time a user needs to make a prediction
