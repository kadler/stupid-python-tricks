#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import feedparser

url = 'http://ibmsystemsmag.com/CMSTemplates/IBMSystemsMag/Feeds/Open-Your-i.aspx'
feed = feedparser.parse(url)

for entry in feed['entries'][:5]:
    print(entry['title'])
    print(entry['link'])
    print()
