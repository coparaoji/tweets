#!/bin/bash

source ./venv/bin/activate

export FLASK_APP=app.py

# put cronjob

flask run

# remove cronjob

deactivate
