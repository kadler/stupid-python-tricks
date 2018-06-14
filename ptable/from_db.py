#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from prettytable import from_db_cursor
import ibm_db_dbi as db2 
from sys import argv

conn = db2.connect()
cur = conn.cursor()

cur.execute(" ".join(argv[1:]))

print(from_db_cursor(cur))
