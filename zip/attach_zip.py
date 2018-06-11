#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from sys import argv, exit
from os.path import basename
from zipfile import ZipFile
from io import BytesIO
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

SERVER = 'smtp.example.com'
FROM = 'sysadmin@example.com'
TO = 'bugwriter@example.com'

if SERVER == 'smtp.example.com':
    print('Please configure the SMTP and sender info', file=sys.stderr)
    exit(1)

smtp = smtplib.SMTP(SERVER)
msg = MIMEMultipart()
msg['Subject'] = 'Application Crashed. Fix now!'
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText('Your code has bugs. Logs attached.'))

zipbuf = BytesIO()
with ZipFile(zipbuf, 'w') as myzip:
    for arg in argv[1:]:
        myzip.write(arg, basename(arg))

# Go to the beginning of the buffer
zipbuf.seek(0);

part = MIMEApplication(zipbuf.read())
part['Content-Disposition'] = 'attachment; filename="logs.zip"'
msg.attach(part)

smtp.send_message(msg)
smtp.quit()
