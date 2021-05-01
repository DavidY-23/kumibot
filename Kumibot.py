import tweepy as tp
import time
import os
import random

from os import environ 

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

#credentials for Twitter

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tp.API(auth)

def func():
    os.chdir('Kumiko')
    for kumiko in os.listdir('.'):
        kumiko = random.choice(os.listdir('.'))
        api.update_with_media(kumiko, status="Kumiko Oumae")
        time.sleep(1800)
func()