# Python parser for average performance evaluation

import sys
import re
import numpy as np

file_path_r = sys.argv[1]
file_path_w = sys.argv[2]

fr = open(file_path_r, 'r')
fw = open(file_path_w, 'w')

'''
readseq   :     244.051 micros/op 4097 ops/sec;   17.0 MB/s (5000000 of 5000000 found)
'''

_parser = 'readseq'
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
