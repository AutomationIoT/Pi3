# Import FLask
from flask import Flask

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

@app.route("/")
def root():
    return "Hello World!"

@app.route("/me")
def rootme():
    return "Hello Me!"
