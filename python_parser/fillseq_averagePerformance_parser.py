# Python parser for average performance evaluation

import sys
import re
import numpy as np

file_path_r = sys.argv[1]
file_path_w = sys.argv[2]

fr = open(file_path_r, 'r')
fw = open(file_path_w, 'w')

'''
fillseq   :       8.510 micros/op 117510 ops/sec;  121.9 MB/s
'''

_parser = 'fillseq'
_init_pattern='^=+'
_init = re.compile(_init_pattern)

_pattern='\S.\S|\S.\S'
__parser = re.compile(_pattern)

line = None
counter = 0

while line != '':
    line = fr.readline()
    mylist = line.split(' ')
    #if _init.match(mylist[0]) != None:
        #fw.write(''.join(mylist))
    if mylist[0] == _parser:
        stringbuilder = []
        mylist = ' '.join(mylist)
        mylist = mylist.split()
        #print(mylist)
        fw.write(','.join(mylist))
fr.close()
fw.close()
