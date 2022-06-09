from flask import Flask
import os,sys
SCRIPT_DIR = os.path.dirname(os.path.abspath('factory.py'))
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))


def create_app():
   app = Flask(__name__)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////databases/tweets'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
   from tweets.utilities.model import db
   db.init_app(app)
   return app