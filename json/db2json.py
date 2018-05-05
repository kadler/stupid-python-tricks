#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ibm_db_dbi as db2
import json

query = "select JSON_OBJECT('name': lstnam, 'limit': cdtlmt) AS object from qiws.qcustcdt"

conn = db2.connect()
cur = conn.cursor()
cur.execute(query)

for row in cur:
    obj = json.loads(row[0])
    print(f'{obj["name"]}: {obj["limit"]}')
