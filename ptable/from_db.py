#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from prettytable import from_db_cursor
import ibm_db_dbi as db2 

conn = db2.connect()
cur = conn.cursor()

cur.execute("select cusnum, lstnam, cdtlmt, baldue, cdtdue from qiws.qcustcdt")

print(from_db_cursor(cur))
