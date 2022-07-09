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
   return render_template('index.html', data=data)



if __name__ == '__main__':
   app.run(debug=True)

@app.cli.command()
def tweet_fetch():
   """A method to fetch tweets"""
   from src import tweets
   from tweets.db import dbs
   from tweepy import TooManyRequests

   list_of_players = dbs.get_players()
   c = tweets.Tweets()
   conn = dbs.create_connection("db/tweets.db")

   for player in list_of_players:
      
      try:
         ids,texts,dates = c.search_player(player[0],(0,0,10))
      except TooManyRequests:
         print("Rate limit exceeded. Try again in 15 minutes")
         return
      except Exception as e:
         print(e)
      
      num_tweets = len(ids)
      print(f'Fetched {num_tweets} tweets for {player[0]}')
      if(num_tweets>0):
         for idx in range(num_tweets):
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
                  except Exception as e:
                     print(e)
                     continue
