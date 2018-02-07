#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import commands
from access import *


def get_auth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return auth


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # When a tweet is published it arrives here.
        print(status.user.screen_name)
        print(status.text)  # Console output may not be UTF-8
        commands.getoutput('python3 SS.py')
        img = 'screenshot.png'
        #mensaje = "Hola .@" + str(status.user.screen_name) + " aquí una captura de pantalla..."
        mensaje1 = "Hola .@" + str(status.user.screen_name)
        api.update_status(mensaje1)
        #api.update_with_media(img, status=mensaje)
        print("-"*10)
        


if __name__ == '__main__':

    # Get an API item using tweepy
    auth = get_auth()  # Retrieve an auth object using the function 'get_auth' above
    api = tweepy.API(auth)  # Build an API object.
    #api.update_status('Hola')
    # Connect to the stream
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    print(">> tweets con @josetrejo25_ #starwars")
    myStream.filter(track=['@josetrejo25_ #starwars'])

