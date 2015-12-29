# coding: utf-8

import flask

import auth
import config
import model
import util
#import requests
#from twython import Twython 
#import twitter

from main import app

###############################################################################
# Tweets
###############################################################################
@app.route('/tweets.json')
@auth.login_required
def tweets():
  user_db = auth.current_user_db()
  tokenTemp = "11985982-nhHMFIftu9DnbRWupF4chVVWRHEIDYEPB1mTcInFB".split('-') #user_db.twitterToken.split('-')
  access_token = tokenTemp[0]
  access_token_secret = tokenTemp[1]
 #twitter = Twython(config.CONFIG_DB.twitter_consumer_key, config.CONFIG_DB.twitter_consumer_secret,access_token, access_token_secret)
 # tweets = twitter.get_home_timeline(count=200)
  #api = twitter.Api(consumer_key=config.CONFIG_DB.twitter_consumer_key, consumer_secret=config.CONFIG_DB.twitter_consumer_secret, access_token_key=access_token, access_token_secret=access_token_secret)
  #tweets = api.GetUserTimeline(screen_name='luca')

  return flask.render_template('tweets.json', html_class='tweets', user_db=user_db,tweets=tweets,)
