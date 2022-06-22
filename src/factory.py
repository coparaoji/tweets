"""A factory script to get flask app.

This file will need flask to be installed.
"""


from flask import Flask
import os,sys
SCRIPT_DIR = os.path.dirname(os.path.abspath('factory.py'))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from flask_sqlalchemy import SQLAlchemy

def create_app():
   """A function to get a Flask app instance.
   
   Returns:
      A flask app instance."""
   template_dir = os.path.abspath('public/templates')
   app = Flask(__name__, template_folder=template_dir)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////..db/tweets'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
   db = SQLAlchemy()
   db.init_app(app)
   return app