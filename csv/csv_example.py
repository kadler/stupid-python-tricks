#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ibm_db_dbi as db2
from csv import writer, QUOTE_NONNUMERIC

conn = db2.connect()
cur = conn.cursor()
cur.execute("select cusnum, lstnam, init, cdtlmt from qiws.qcustcdt where cdtlmt > 100")

with open('qcustcdt.csv', 'w', newline='') as file:
    csvf = writer(file, quoting=QUOTE_NONNUMERIC)
    for row in cur:
        csvf.writerow(row)
