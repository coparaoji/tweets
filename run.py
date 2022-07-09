#!venv/bin/python

import multiprocessing
import time
import os

def run_app():
    #run app
    os.system("pwd")
    print("Starting app.")
    os.system("flask run")

def background():
    os.system('echo "fetching tweets in 10 seoconds..."')
    while True:
        time.sleep(10)
        os.system("flask tweet-fetch")


if __name__ == '__main__':
    mainApp = multiprocessing.Process(target=run_app)
    background_task = multiprocessing.Process(target=background, daemon=True)
    os.system("export FLASK_APP=app.py")
    background_task.start()
    #mainApp.start()
    run_app()
