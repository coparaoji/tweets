# -----------------------------------------------------------
# File for handling and getting the setiment of the tweets.
#
# This file should be updated to us AWS targeted Sentiment instead of 
# 2022 Alex Oparaoji
# email coparaoji@gmail.com
# -----------------------------------------------------------
import os
from google.cloud import language_v1

class Sentiment_getter:
    '''
    This is the class for all sentiment needs.
    It will need to handle retrieveal to a databae as well.
    '''

    # This key will be changed to a key with less permissions
    path_to_cient_key = "/home/alex/GreyCroc/Braindump/secure_keys/serene-gradient.json" 
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path_to_cient_key

    # Instantiates a client
    client = language_v1.LanguageServiceClient()

    def __init__(self) -> None:
        pass


    def get_sentiment(self, text:str)->tuple:
        """
        This function getst the sentiment of the text it's given
        """
        # The text to analyze
        document = language_v1.Document(
            content=text, type_=language_v1.Document.Type.PLAIN_TEXT
        )

        # Detects the sentiment of the text
        sentiment = self.client.analyze_sentiment(
            request={"document": document}
        ).document_sentiment

        return (sentiment.score, sentiment.magnitude)
