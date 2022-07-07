#!venv/bin/python

import multiprocessing
import time
import os

def run_app():
    #run app
    os.system("pwd")
    os.system("flask run")

def background():
    time.sleep(10)
    os.system('echo "fetching tweets"')
    while True:
        os.system("flask tweet-fetch")
        time.sleep(10)



mainApp = multiprocessing.Process(target=run_app)
background_task = multiprocessing.Process(target=background, daemon=False)
os.system("export FLASK_APP=app.py")

mainApp.start()
background_task.start()
