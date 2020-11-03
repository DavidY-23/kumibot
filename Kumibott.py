import tweepy as tp
import time
import os
import random

#login to Twitter dot com
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tp.API(auth)


os.chdir('Kumiko')
for kumiko in os.listdir('.'):
    kumiko = random.choice(os.listdir('.'))
    api.update_with_media(kumiko)
    time.sleep(1800)