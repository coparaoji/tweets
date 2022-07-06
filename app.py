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

@app.cli.command()
def tweet_fetch():
   from src import tweets
   from tweets.db import dbs

   list_of_players = dbs.get_players()
   c = tweets.Tweets()
   tweets_queue = []
   conn = dbs.create_connection("db/tweets.db")
   for player in list_of_players:
      ids,texts,dates = c.search_player(player[0],(0,0,60))
      if(len(texts)>0):
         tweet_dict = {player[1]:(ids,texts,dates)}
         tweets_queue.append(tweet_dict)
         for idx,tweet in enumerate(ids):
               unique_id = player[1]+str(ids[idx])
               tweet_id = ids[idx]
               player_id = player[1]
               score,mag = (0,0)
               resultant = score*mag
               created_at=str(dates[idx])
               record = (unique_id,tweet_id,player_id,texts[idx],score,mag,resultant,created_at)
               with conn:
                  try:
                     dbs.create_tweet(conn,record)
                     print('1 success')
                  except Exception as e:
                     print(e)
                     continue
