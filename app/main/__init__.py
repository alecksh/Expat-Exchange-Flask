# Blueprint creation

from flask import Blueprint

#Blueprints are created by instantiating an object of class Blueprint
#This constructor takes two required arguments: the blueprint name and the module or package
#where the blueprint is located
main = Blueprint('main', __name__)

from . import views, errors

#The modules are imported at the bottom to avoid circular dependencies, because views.py and errors.py need
#to import the main blueprint

#The blueprint is registered with the application inside the create_app() factory function (app/__init__.py)
