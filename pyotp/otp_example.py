#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pyotp
import time

key = pyotp.random_base32()
print(key)

totp = pyotp.TOTP(key)

print(totp.now())
time.sleep(60)
print(totp.now())
