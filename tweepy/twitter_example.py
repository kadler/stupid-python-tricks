#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tweepy
from os import environ

# Set up your info here: 
CONSUMER_KEY = environ["CONSUMER_KEY"]
CONSUMER_SECRET = environ["CONSUMER_SECRET"]
ACCESS_TOKEN = environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
results = api.search("#PowerUP18")

for result in results[:5]:
    print('@' + result.user.screen_name + ':')
    print(result.text)
    print()
