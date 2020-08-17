import json
import random
import tweepy
import credentials
import sys
from os import environ
def get_quotes():
    with open ("C:\\Users\\tuxbu\\words\\data.json") as f:
        quotes_json = json.load(f)
    return quotes_json["quotes"]
consumer_key = environ["API_KEY"]
consumer_secret_key = environ["API_SECRET_KEY"]
access_token = environ["ACCESS_TOKEN"]
access_token_secret = environ["ACCESS_TOKEN_SECRET"]
def get_random_quote():
    quotes = get_quotes()
    random_quote = random.choice(quotes)
    return random_quote
def create_tweet():
    quote = get_random_quote()
    tweet = """
            {}
            """.format(quote["quote"])
    return tweet
def tweet_quote():
    interval = 60 * 60 * 4

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    while True:
        print("getting a random quote...")
        tweet = create_tweet()
        api.update_status(tweet)
        time.sleep(interval)

if __name__ == "__main__":
    tweet_quote()
