import tweepy
from config import consumerKey, consumerSecret, accessToken, accessTokenSecret

def tweet_init(blurb):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler( consumerKey , consumerSecret )
    auth.set_access_token(accessToken, accessTokenSecret)
    # Create API object
    api = tweepy.API(auth)
    # Create a tweet
    api.update_status(blurb)

