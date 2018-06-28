# *** REMINDER:
# if running locally, set global variable
# in terminal: export FLASK_APP=application.py


#import Flask class from flask library
from flask import Flask

# initialize an instance of Flask class ClassName(object):
app = Flask(__name__)

# return hello, world message on index page
@app.route('/')
def index():
    return 'Hello, World!'
