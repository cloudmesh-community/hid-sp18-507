# Using Tweepy's Module for pulling API data
# http://docs.tweepy.org/en/v3.5.0/api.html#api-reference

from tweepy import OAuthHandler
from tweepy import API
import tweepy
import twittercredentials
from pymongo import MongoClient

# Authorization for Querying Twitter's API
auth = OAuthHandler(twittercredentials.CONSUMER_KEY, twittercredentials.CONSUMER_SECRET)
auth.set_access_token(twittercredentials.ACCESS_TOKEN, twittercredentials.ACCESS_TOKEN_SECRET)

api = API(auth)

# Number of returned tweets
return_count = 500

data = {}


def twitterscrape(search_term):
    searched_tweets = [status._json for status in
                       tweepy.Cursor(api.search,  q=search_term, lang="en").items(return_count)]

    return searched_tweets


def main():
    # client = MongoClient("mongodb://localhost:27017/")
    # connection = pymongo.Connection("mongodb://localhost", safe = True)
    # query = str(input(What search term/hashtag would you like to scrape?))
    client = MongoClient("mongodb+srv://hidsp18507:hidsp18507!@cluster524-vl3t1.mongodb.net/twitter")
    query = "#LockHerUp"
    scrape = twitterscrape(query)
    db = client.twitter

    # Adds the scraped tweets to MongoDB Atlas cloud
    for i in scrape:
        db.tweets.insert_one({'_id' : i['id'], 'data' : i})



if __name__ == '__main__':
    main()
