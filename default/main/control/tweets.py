# coding: utf-8

import flask

import auth
import config
import model
import util
#from twython import Twython 

from main import app

###############################################################################
# Tweets
###############################################################################
@app.route('/tweets.json')
@auth.login_required
def tweets():
  user_db = auth.current_user_db()
  tokenTemp = user_db.twitterToken.split('-')
  access_token = tokenTemp[0]
  access_token_secret = tokenTemp[1]
 #twitter = Twython(config.CONFIG_DB.twitter_consumer_key, config.CONFIG_DB.twitter_consumer_secret,access_token, access_token_secret)
 # tweets = twitter.get_home_timeline(count=200)
  return flask.render_template('tweets.json', html_class='tweets', user_db=user_db,)
