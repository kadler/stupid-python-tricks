#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bottle import request, get, post, run, view
import bottle
import ibm_db_dbi as db2

@get('/')
def root():
    return bottle.template('index')

@post('/query')
@view('query')
def query():
    cur = db2.connect().cursor()
    cur.execute(request.forms.get('sql'))
    return {'rows': cur}

run(host='0.0.0.0', port=9000)
