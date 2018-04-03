# Using Tweepy's Module for pulling API data
# http://docs.tweepy.org/en/v3.5.0/api.html#api-reference

from tweepy import OAuthHandler
from tweepy import API
import tweepy
import twitter_credentials
import pprint
import json
import time
import datetime

import pymongo
from pymongo import MongoClient

# Authorization for Querying Twitter's API
auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

api = API(auth)

# Number of returned tweets
return_count = 200

data = {}


def twitterscrape(search_term):
	

	searched_tweets = [status._json for status in tweepy.Cursor(api.search,  q=search_term, lang="en").items(return_count)]
	#pprint.pprint(searched_tweets[:])
	#print(type(searched_tweets[:]))
	# for tweet in searched_tweets:

	# 	# pprint.pprint(tweet)

	# 	# User Info
	# 	ID = str(tweet['user']['id'])
	# 	username = tweet['user']['screen_name']

	# 	# Followers vs Friends
	# 	followerCT = tweet['user']['followers_count']
	# 	friendCT = tweet['user']['friends_count']
	# 	ffratio = float(followerCT/friendCT)

	# 	# Age of account vs Posts
	# 	account_start = tweet['user']['created_at']
	# 	account_created = datetime.datetime.strptime(account_start, '%a %b %d %H:%M:%S +0000 %Y')
	# 	account_age = (datetime.datetime.now()-account_created).days
	# 	total_posts = tweet['user']['statuses_count']
	# 	favouritesCT = tweet['user']['favourites_count']
	# 	postperday = float(total_posts/account_age)
	# 	favsperday = float(favouritesCT/account_age)

	# 	# Actual Tweet Pulled
	# 	tweet_text = tweet['text']

	# 	#post_platform = tweet['source']

	# 	# Disctionary / JSON creation
	# 	data[ID] = {'id' : ID,\
	# 			   'username' : username,\
	# 		       'followers_count' : followerCT,\
	# 			   'friends_count' : friendCT,\
	# 			   'creation_date': str(account_created),\
	# 			   'account_age' : account_age,\
	# 			   'total_posts' : total_posts,\
	# 			   'total_favourites' : favouritesCT,\
	# 			   'calculations' : {'ffratio' : ffratio,\
	# 			   					 'account_age' : account_age,\
	# 			   					 'posts_per_day' : postperday,\
	# 			   					 'favs_per_day' : favsperday},\
	# 			   	'text' : tweet_text
	# 				}

	# #pprint.pprint(data)
	# return data
	return searched_tweets


def main():
	client = MongoClient("mongodb+srv://giuliani-test:<PASSWORD>@cluster524-vl3t1.mongodb.net/twitter")
	#client = MongoClient("mongodb://localhost:27017/")
	#connection = pymongo.Connection("mongodb://localhost", safe = True)
	# query = str(input(What search term/hashtag would you like to scrape?))
	query = "#MeToo"
	scrape = twitterscrape(query)
	#print(scrape)
	db = client.twitter
	for i in scrape:
		#print(scrape[i],'\n')
		#i.pop('_id', 0)
		#pprint.pprint(i)
		#pprint.pprint(i['id'])
		#ct = 1
		db.tweets.insert_one({'_id' : i['id'], 'data' : i})
		#ct+=1

	#db.tweets.insert_one(scrape)


	# ingest = db.tweets
	# ingest.insert_one(scrape).inserted_id


if __name__ == '__main__':
	main()
