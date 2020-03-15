#Import Flask
from flask import Flask

#Create a new Flask instance called "app"
app = Flask(__name__)

#Creat a Flask route
##Define the starting point aka the "root"
@app.route('/')
def hello_world():
   return 'Hello World'

#Run Flask app via Terminal
#export FLASK_APP=flask_example.py
