from flask import Flask, jsonify, request
from flask.ext.pymongo import PyMongo
import json
import datetime

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'twitter'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/'
app.config['MONGO_URI'] = 'mongodb+srv://giuliani-test:<PASSWORD>@cluster524-vl3t1.mongodb.net/twitter'

mongo = PyMongo(app)

@app.route('/tweets/data', methods = ['GET'])
def get_data():
    tweet = mongo.db.tweets
    output = {}
    for q in tweet.find():
        output[q['data']['id']] = {q['data']['user']['screen_name'] : q['data']}
    return jsonify(output)


@app.route('/users', methods = ['GET'])
def get_users():
    tweet = mongo.db.tweets
    output = {}
    for q in tweet.find():
        output[q['data']['user']['screen_name']] = q['data']['user']
    return jsonify(output)

@app.route('/users/names', methods = ['GET'])
def get_users_names():
    tweet = mongo.db.tweets
    output = {}
    for q in tweet.find():
        output[q['data']['user']['screen_name']] = q['data']['user']['name']
    return jsonify(output)


@app.route('/tweets/text', methods = ['GET'])
def get_text():
    tweet = mongo.db.tweets
    output = {}
    for q in tweet.find():
        output[q['data']['user']['screen_name']] = q['data']['text']
    return jsonify(output)


@app.route('/tweets/userhistory', methods = ['GET'])
def get_user_history():
    tweet = mongo.db.tweets
    output = {}
    for q in tweet.find():
        account_start = q['data']['user']['created_at']
        account_created = datetime.datetime.strptime(account_start, '%a %b %d %H:%M:%S +0000 %Y')
        account_age = (datetime.datetime.now()-account_created).days
        total_posts = q['data']['user']['statuses_count']
        total_faves = q['data']['user']['favourites_count']
        postperday = float(total_posts/account_age)
        favsperday = float(total_faves/account_age)

        output[q['data']['user']['screen_name']] = {'accounts_age' : account_age, 'daily_posts' : postperday, 'daily_faves' : favsperday}
    return jsonify(output)


@app.route('/tweets/ratios', methods = ['GET'])
def get_user_ratios():
    tweet = mongo.db.tweets
    output = {}
    for q in tweet.find():
        followerCT = q['data']['user']['followers_count']
        friendCT = q['data']['user']['friends_count']
        ffratio = float((friendCT+0.00000000000001)/(followerCT+0.00000000000001))

        output[q['data']['user']['screen_name']] = {'friends_per_follows' : ffratio}
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
