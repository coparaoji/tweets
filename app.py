from flask import render_template
import sys
import os
sys.path.append(os.path.dirname('..'))
import src.factory as factory


app = factory.create_app()

@app.route('/', methods=['GET'])
def index():
   from tweets.db import dbs
   data = dbs.get_data()
   #return (f'<p>{ app.template_folder }</p>')
   return render_template('index.html', data=data)



if __name__ == '__main__':
   app.run(debug=True)