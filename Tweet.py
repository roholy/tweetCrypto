import tweepy
import Trade
from config import consumerKey, consumerSecret, accessToken, accessTokenSecret
from Trade import nugget
# Authenticate to Twitter
auth = tweepy.OAuthHandler( consumerKey , consumerSecret )
auth.set_access_token(accessToken, accessTokenSecret)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status(Trade.nugget)

# fetch user data
# user = api.get_user("espn")

# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)

# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)
# for tweet in tweepy.Cursor(api.home_timeline).items(2):
#     print(f"{tweet.user.name} said: {tweet.text}")
# api.update_status(tweet.text)



# added nugget to connect multiple files
print (nugget)