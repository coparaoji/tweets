from flask import render_template
import sys
import os
sys.path.append(os.path.dirname('..'))
import factory


app = factory.create_app()

@app.route('/', methods=['GET'])
def index():
   from utilities import dbs
   data = dbs.get_data()
   return render_template('index.html', data=data)



if __name__ == '__main__':
   app.run(debug=True)