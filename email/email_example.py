#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from sys import argv, exit
from email.mime.text import MIMEText

SERVER = 'smtp.example.com'
FROM = 'sysadmin@example.com'
TO = 'bugwriter@example.com'

if SERVER == 'smtp.example.com':
    print('Please configure the SMTP and sender info', file=sys.stderr)
    exit(1)
    
smtp = smtplib.SMTP(SERVER)

for arg in argv[1:]:
    with open(arg) as file:
        msg = MIMEText(file.read())
        msg['Subject'] = arg
        msg['From'] = FROM
        msg['To'] = TO
        
        smtp.send_message(msg)

smtp.quit()
