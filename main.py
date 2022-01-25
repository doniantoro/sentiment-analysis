import tweepy
import re
from textblob import TextBlob

# Auth twitter API
auth = tweepy.OAuthHandler(<consumer_key>, <consumer_secret>)
auth.set_access_token(<access_token>, <access_token_secret>)

api = tweepy.API(auth)

search = input("Enter a keyword : ")
# Crawling tweet by search
public_tweets = api.search(q=search , lang= "en" , count = "100" )

# Init sentiment variable
sentiment_positif=0
sentiment_negatif=0
sentiment_netral=0

# Looping tweet
for tweet in public_tweets:
    # regex to remove hastag,link and "@"
    content_tweets = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.text).split());

    # determine sentiment with TextBlob
    analysis = TextBlob(content_tweets)
    result_analysis =analysis.sentiment.polarity
    
    # calculate sentiment
    if result_analysis > 0.0 :
       sentiment_positif+=1
    elif result_analysis < 0.0 :
       sentiment_negatif+=1
    elif result_analysis == 0.0 :
       sentiment_netral+=1
      #  print(content_tweets,"")
      #  print("")

    # print (analysis.sentiment.polarity)
print ("Netral Sentiment ",sentiment_netral,"%")
print ("Positif Sentiment ", sentiment_positif,"%")
print ("Negatif Sentiment", sentiment_negatif,"%")
