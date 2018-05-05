#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import *
import ibm_db_dbi as db2
import prettytable

app = Flask(__name__)

@app.template_filter('cursor_to_table')
def cursor_to_table(cursor):
    return prettytable.from_db_cursor(cursor).get_html_string()

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    cur = db2.connect().cursor()
    cur.execute(request.form.get('sql'))
    return render_template('query.html', cursor=cur)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
