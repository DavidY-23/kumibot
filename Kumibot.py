import tweepy as tp
import time
import os
import random
import config

#credentials for Twitter

auth = tp.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tp.API(auth)

def func():
    os.chdir('Kumiko')
    for kumiko in os.listdir('.'):
        kumiko = random.choice(os.listdir('.'))
        api.update_with_media(kumiko, status="Kumiko Oumae")
        time.sleep(1800)
func()