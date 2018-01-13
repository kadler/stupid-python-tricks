#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from prettytable import PrettyTable
x = PrettyTable()


x.field_names = ("City", "Area", "Annual Rainfall")
x.add_row(("Adelaide", 1295, 600.5))
x.add_row(("Brisbane", 5905, 1146.4))
x.add_row(("Darwin", 112, 1714.7))
x.add_row(("Hobart", 1357, 619.5))
x.add_row(("Sydney", 2058, 1214.8))

print(x)
