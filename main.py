import tweepy
import os
import data

consumer_key = os.getenv("CONSUMER_KEY_TWITTER")
consumer_secret = os.getenv("CONSUMER_SECRET_TWITTER")
access_token = os.getenv("ACCESS_TOKEN_TWITTER")
acces_token_secret = os.getenv("ACCESS_TOKEN_SECRET_TWITTER")

client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,
                       access_token=access_token, access_token_secret=acces_token_secret)

tweet = data.tweet()
response = client.create_tweet(
    text=tweet
)

print(f"https://twitter.com/user/status/{response.data['id']}")

