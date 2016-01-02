# coding: utf-8

import flask

import auth
import config
import model
import tweepy
import json
from flask import request

from main import app

###############################################################################
# Tweets
###############################################################################



@app.route('/tweets.json')
@auth.login_required
def tweets():
  max_tweet_id = request.args.get('max_id')
  user_db = auth.current_user_db()
 
  authy = tweepy.OAuthHandler(config.CONFIG_DB.twitter_consumer_key, config.CONFIG_DB.twitter_consumer_secret)
  authy.set_access_token(user_db.twitterToken, user_db.twitterSecret)
  
  api = tweepy.API(authy)
  if max_tweet_id != '0':
    tweets = api.home_timeline(count=30, max_id=max_tweet_id)
  else:
    tweets = api.home_timeline(count=30)
  tweetstring = '{"tweets":['
  for status in tweets:
     tweetstring += '{"status":'+json.dumps(status.text)+',"account":"'+status.user.screen_name+'","avatar":"'+status.user.profile_image_url+'", "id":"'+status.id_str+"'},'
     max_tweet_id = status.id_str
  tweetstring = tweetstring[:-1] #removing that last ',' to get valid json
  tweetstring += '], "max_tweet_id":"'+max_tweet_id+'"}'
    
  return flask.render_template('tweets.json', html_class='tweets',tweets=tweetstring,)
