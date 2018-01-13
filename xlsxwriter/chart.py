#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from xlsxwriter import Workbook

with Workbook('test.xlsx') as workbook: 
    ws = workbook.add_worksheet()
    ws.write_column('A1', [10, 93, 42, 59, 34])

    chart = workbook.add_chart({'type': 'line'})
    chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
    
    ws.insert_chart('C1', chart)
