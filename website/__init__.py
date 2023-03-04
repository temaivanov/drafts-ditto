#__init__.py to make the website folder a python package
from flask import Flask 

#setting up Flask goes here
def create_app():
    app = Flask(__name__) #https://blog.miguelgrinberg.com/post/why-do-we-pass-name-to-the-flask-class
    app.config.from_pyfile('../config.py') #https://hackersandslackers.com/configure-flask-applications/ should I put .env into a .gitignore?

    return app