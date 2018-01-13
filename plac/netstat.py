#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ibm_db_dbi as db2
from prettytable import from_db_cursor

def main(port: ("Local port", 'option')):
    "NETSTAT in Python using plac"
    
    sql = 'SELECT CONNECTION_TYPE, LOCAL_ADDRESS, LOCAL_PORT, JOB_NAME FROM QSYS2.NETSTAT_JOB_INFO'
    params = []
    
    if port:
        sql += ' WHERE LOCAL_PORT = ?'
        params.append(port)
    
    conn = db2.connect()
    cur = conn.cursor()
    cur.execute(sql, params)
    print(from_db_cursor(cur))

if __name__ == '__main__':
    import plac; plac.call(main)
