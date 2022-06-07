# -----------------------------------------------------------
# File for handling and getting the setiment of the tweets
#
# 2022 Alex Oparaoji
# email coparaoji@gmail.com
# -----------------------------------------------------------

from tweepy import Client
import datetime

bearer_token ='AAAAAAAAAAAAAAAAAAAAAHLNcgEAAAAAcT1066CikEPelcTlLn4Aie%2FMOZQ%3DFnJ57W2cK6opwqifsi9JfjuODqsFDE2x25rTtQNjNOSsVCjtlx'

class Tweets:
    """
    This makes searches for tweets and updates the databases
    """
    client = Client(bearer_token=bearer_token) 
    
    def __init__(self):
        pass

    def search_player(self,player_name):
        # This is for searching players with the twitter api.
        end_datetime = datetime.datetime.today() - datetime.timedelta(days=6)

        query = f'(entity:"{player_name}" OR "{player_name}") -is:retweet lang:en'

        response =  self.client.search_recent_tweets(
        query=query,
        start_time=end_datetime,
        sort_order='relevancy',
        max_results=100,
        tweet_fields= 'created_at'
        )

        ids,texts,dates=[],[],[]
        for tweet in response.data:
            ids.append(tweet.id)
            texts.append(tweet.text)
            dates.append(tweet.created_at)

        return (ids, texts, dates)

 