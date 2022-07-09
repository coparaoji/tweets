# -----------------------------------------------------------
# File for handling and getting the setiment of the tweets
#
# 2022 Alex Oparaoji
# email coparaoji@gmail.com
# -----------------------------------------------------------

from tweepy import Client
import datetime
import os

os.environ['BEARER_TOKEN'] ='AAAAAAAAAAAAAAAAAAAAAHLNcgEAAAAAcT1066CikEPelcTlLn4Aie%2FMOZQ%3DFnJ57W2cK6opwqifsi9JfjuODqsFDE2x25rTtQNjNOSsVCjtlx'

class Tweets:
    """
    This makes searches for tweets and updates the databases
    """
    client = Client(bearer_token=os.environ.get('BEARER_TOKEN')) 
    
    def __init__(self):
        pass

    def search_player(self,player_name, time_back = (6,0,0)):
        ''' This is for searching players with the twitter api. '''


        end_datetime = datetime.datetime.today() - datetime.timedelta(days=time_back[0], hours=time_back[1], seconds=time_back[2])
        end_datetime = end_datetime.astimezone(datetime.timezone.utc)

        query = f'(entity:"{player_name}" OR "{player_name}") -is:retweet lang:en'
    
        response =  self.client.search_recent_tweets(
        query=query,
        start_time=end_datetime,
        sort_order='relevancy',
        max_results=100,
        tweet_fields= 'created_at'
        )
        ids,texts,dates=[],[],[]

        if(response.data != None):
            for tweet in response.data:
                ids.append(tweet.id)
                texts.append(tweet.text)
                dates.append(tweet.created_at)

        return (ids, texts, dates)
    

 