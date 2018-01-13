#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bottle import request, response, get, run
import qrcode
import pyotp
import io

@get('/')
def root():
    key = request.query.get('key', 'XK3I4RJ3OY7M7DAY')
    totp = pyotp.TOTP(key)
    qr = qrcode.make(totp.provisioning_uri('pyqrcode'))
    imgbuf = io.BytesIO()
    qr.save(imgbuf, format='PNG')

    response.content_type ='image/png'

    return imgbuf.getvalue()

run(host='0.0.0.0', port=9000)
