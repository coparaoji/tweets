# -----------------------------------------------------------
# File testing functionality
#
# 2022 Alex Oparaoji
# email coparaoji@gmail.com
# -----------------------------------------------------------

import sentiments as senti

senti_getter = senti.Sentiment_getter()

text = "The celtics big three of Tatum, Brown, and Smart may have what it takes to win the finals"

print(text)

score, = senti_getter.get_sentiment(text)

print(f"the sentiment score is {score}")
