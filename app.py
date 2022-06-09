from contextlib import redirect_stderr
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////databases/tweets'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'


class Tweet(db.Model):
    __name__ = 'tweet'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(241), nullable=False)
    player_id = db.Column(db.String(50), unique=True, nullable=False)
    sentiment_score = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return (f"<Tweets id:{id} text:{text} created_at:{created_at}")


@app.route('/', methods=['POST', 'GET'])
def index():
   if False:

      #create a new task from form input
      task_content =request.form['content']
      new_task = Todo(content = task_content)
      
      #try to commit to database then redirect back to home
      try:
         db.session.add(new_task)
         db.session.commit()
         return redirect('/')
      except:
         return 'There was en issue adding your task'
   else:

      #look at created items in database and return 
      #tasks = Todo.query.order_by(Todo.date_created).all()
      return render_template('index.html')#, tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
   
   #get task or give 404
   task_to_delete = Todo.query.get_or_404(id)
   
   #attaempt to deletefrom database
   try:
      db.session.delete(task_to_delete)
      db.session.commit()
      return redirect('/')
   except:
      return 'There was an issue deleting that task'

@app.route('/update/<int:id>',methods=['GET',"POST"])
def update(id):
   task = Todo.query.get_or_404(id)

   if request.method == 'POST':
      #update logic when button is pressed
      task.content = request.form['content']

      #try to commit to database
      try:
         db.session.commit()
         return redirect('/')
      except:
         return 'There was an issue updating your task.'
   else:
      return render_template('update.html', task=task)
  

if __name__ == '__main__':
   app.run(debug=True)