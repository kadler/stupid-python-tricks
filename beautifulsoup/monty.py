#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen

u = 'http://imdb.com/title/tt0071853/fullcredits'
resp = urlopen(u)

soup = BeautifulSoup(resp.read(), 'html.parser')

top_cast = soup.find_all('td', 'itemprop')[:6]
names = [actor.span.string for actor in top_cast]

for name in names:
    print(name)
