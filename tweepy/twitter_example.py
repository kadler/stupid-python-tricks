#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tweepy
from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q="#NHMUG").items(4):
    print('@' + tweet.user.screen_name + ':')
    print(tweet.text, "\n")
