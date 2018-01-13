#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

def usd_to_btc(usd_m):
    return round(usd_m * 1000000 / 14289, 2)

conn = sqlite3.connect('my.db')

#                    name,  #parms, func
conn.create_function('btc',      1, usd_to_btc)

cur = conn.cursor()
cur.execute("select movie, gross, btc(gross) from mytable")

for row in cur:
     print(row)

