#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from xlsxwriter import Workbook
import ibm_db_dbi as db2

cur = db2.connect().cursor()
cur.execute("select cusnum, lstnam, cdtlmt, baldue, cdtdue from qiws.qcustcdt")

headers = [desc[0] for desc in cur.description]

with Workbook('qcustcdt_format.xlsx') as workbook:
    fmt = workbook.add_format({'font_size': 20})

    hdr_fmt = workbook.add_format({'font_size': 20, 'align':'center', 'border':1})
    red_fmt = workbook.add_format({'font_size': 20, 'bg_color': '#FF0000'})

    ws = workbook.add_worksheet()

    ws.conditional_format("D2:D13", {'type': 'cell',
                                     'criteria': '>',
                                     'value': 'C2*0.5',
                                     'format': red_fmt})

    ws.set_column(0, len(headers)-1, 16)

    ws.write_row('A1', headers, hdr_fmt)
    ws.set_row(0, 22)

    for rownum, row in enumerate(cur, start=1):
        ws.write_row(rownum, 0, row)
        ws.set_row(rownum, 22, fmt)
