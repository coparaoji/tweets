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
    """This makes searches for tweets and updates the databases.

    Attributes:
        client: a Tweepy class, Client.
    """
    client = Client(bearer_token=bearer_token) 

    def search_player(self,player_name):
        """This is for searching players with the twitter api.
        
        Args:
            player_name: A string in the format: first_name last_name
            
        Returns:
            A tuple of tweet IDs, texts, and origin date.
            For example:
            
            (
             [12,14],
             ['Jordan Poole is a future all-star',
               'Poole has developed really well'],
             ['2022-06-06 03:11:12+00:00',
              '2022-06-03 14:00:01+00:00']
            )
              
            """

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

 