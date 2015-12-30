# coding: utf-8

import flask

import auth
import config
import model
import util
import twitter
import tweepy

from main import app

###############################################################################
# Tweets
###############################################################################



@app.route('/tweets.json')
@auth.login_required
def tweets():
  user_db = auth.current_user_db()
  
 #twitter = Twython(config.CONFIG_DB.twitter_consumer_key, config.CONFIG_DB.twitter_consumer_secret,access_token, access_token_secret)
 # tweets = twitter.get_home_timeline(count=200)
  #api = twitter.Api(consumer_key=config.CONFIG_DB.twitter_consumer_key, consumer_secret=config.CONFIG_DB.twitter_consumer_secret, access_token_key=access_token, access_token_secret=access_token_secret, cache=None)
  #tweets = api.GetUserTimeline(screen_name='luca')
  authy = tweepy.OAuthHandler(config.CONFIG_DB.twitter_consumer_key, config.CONFIG_DB.twitter_consumer_secret)
  authy.set_access_token(user_db.twitterToken, user_db.twitterSecret)

  api = tweepy.API(authy)

  tweets = api.home_timeline()
  return flask.render_template('tweets.json', html_class='tweets',tweets=tweets,)
