#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import qrcode

url = 'http://google.com'
qr = qrcode.make(url)
qr.save('qr.png')
