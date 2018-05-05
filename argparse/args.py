#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from os import system

parser = ArgumentParser(description='HTTP Admin')

parser.add_argument('--action', required=True, \
    choices=('start', 'stop', 'restart'), \
    help='Server Action')

parser.add_argument('--server', default='*ALL', \
    help='Server to act on')

args = parser.parse_args()

cmd = {
    'start':   'STRTCPSVR',
    'stop':     'ENDTCPSVR',
    'restart': 'STRTCPSVR',
}[args.action]

cl = f"{cmd} SERVER(*HTTP) HTTPSVR({args.server})"
if args.action == 'restart':
    cl += ' RESTART(*HTTP)'

print(cl)
system(f'system "{cl}"')

