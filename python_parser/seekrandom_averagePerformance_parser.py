# Python parser for average performance evaluation

import sys
import re
import numpy as np

file_path_r = sys.argv[1]
file_path_w = sys.argv[2]

fr = open(file_path_r, 'r')
fw = open(file_path_w, 'w')

'''
seekrandom   :      25.816 micros/op 38736 ops/sec; (6848249 of 6848249 found)
'''

_parser = 'seekrandom'
_init_pattern='^=+'
_init = re.compile(_init_pattern)

_pattern='\S.\S|\S.\S'
__parser = re.compile(_pattern)

line = None
counter = 0

while line != '':
    line = fr.readline()
    mylist = line.split(' ')
    if mylist[0] == _parser:
        mylist = ' '.join(mylist)
        mylist = mylist.split()
        fw.write(','.join(mylist))
fr.close()
fw.close()
