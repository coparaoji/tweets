from flask import Flask
import os,sys
sys.path.append(os.path.dirname('..'))
from src import tweets

SCRIPT_DIR = os.path.dirname(os.path.abspath('factory.py'))
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))

class Config:
   SQLALCHEMY_DATABASE_URI = 'sqlite:////..db/tweets'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   SCHEDULER_API_ENABLED = True

def create_app():
   template_dir = os.path.abspath('public/templates')
   app = Flask(__name__, template_folder=template_dir)
   app.config.from_object(Config())
   from tweets.src.model import db
   db.init_app(app)
   return app