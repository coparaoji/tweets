from flask import Flask
import os,sys
SCRIPT_DIR = os.path.dirname(os.path.abspath('factory.py'))
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))


def create_app():
   template_dir = os.path.abspath('public/templates')
   app = Flask(__name__, template_folder=template_dir)
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////..db/tweets'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
   from tweets.src.model import db
   db.init_app(app)
   return app