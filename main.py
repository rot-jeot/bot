#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from access import *


def get_auth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return auth


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # When a tweet is published it arrives here.
        print(status.user.screen_name)
        print(status.text)       
        mensaje = "Hola @" + str(status.user.screen_name)
        api.update_status(mensaje)
        print("-"*15)
        


if __name__ == '__main__':

    # Get an API item using tweepy
    auth = get_auth()  # Retrieve an auth object using the function 'get_auth' above
    api = tweepy.API(auth)  # Build an API object.
    #api.update_status('Hola')
    # Connect to the stream
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    print("**** tweets con @Usiario ****")
    myStream.filter(track=['@usuario'])

