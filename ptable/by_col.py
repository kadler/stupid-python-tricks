#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from prettytable import PrettyTable
x = PrettyTable()

x.add_column("City", ["Adelaide", "Brisbane", \
                "Darwin", "Hobart", "Sydney"])

x.add_column("Area", \
                [1295, 5905, 112, 1357, 2058])

x.add_column("Annual Rainfall", \
       [600.5, 1146.4, 1714.7, 619.5, 1214.8])

print(x)
