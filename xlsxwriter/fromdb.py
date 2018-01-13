#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from xlsxwriter import Workbook
import ibm_db_dbi as db2

conn = db2.connect()
cur = conn.cursor()

cur.execute("select cusnum, lstnam, cdtlmt, baldue, cdtdue from qiws.qcustcdt")
headers = [descr[0] for descr in cur.description]
    
with Workbook('qcustcdt.xlsx') as workbook:
    ws = workbook.add_worksheet()
    ws.write_row('A1', headers)

    for row, data in enumerate(cur, start=1):
        ws.write_row(row, 0, data)
