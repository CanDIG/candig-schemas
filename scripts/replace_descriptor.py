#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Some protoc versions put "file=DESCRIPTOR" into the models
"""

import glob

filenames = glob.glob('../python/candig/schemas/*/*pb2.py')

for filename in filenames:
    print(filename)
    with open(filename, 'r') as df:
        lines = df.readlines()
        
    new = ''
    for line in lines:
        new = ''.join((new, line.replace(', file=DESCRIPTOR', '')))
    
    with open(filename, 'w') as df:
        df.write(new)


