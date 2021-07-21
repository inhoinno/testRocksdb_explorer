# Python parser for average performance evaluation

import sys
import re
import numpy as np

file_path_r = sys.argv[1]
file_path_w = sys.argv[2]

fr = open(file_path_r, 'r')
fw = open(file_path_w, 'w')

'''
readrandom   :     244.051 micros/op 4097 ops/sec;   17.0 MB/s (5000000 of 5000000 found)
'''

_parser = 'readrandom'
_init_pattern='^=+'
_init = re.compile(_init_pattern)

_pattern='\S.\S|\S.\S'
__parser = re.compile(_pattern)

line = None
counter = 0

while line != '':
    line = fr.readline()
    mylist = line.split(' ')
    if _init.match(mylist[0]) != None and counter == 0:
        fw.write(''.join(mylist))
    if mylist[0] == _parser:
        stringbuilder = []
        mylist = ' '.join(mylist)
        mylist = mylist.split()
        for i in np.arange(0, len(mylist[2:8]), 2):
            if __parser.match(mylist[3+i]) != None:
                stringbuilder.append(__parser.search(mylist[2+i]).group(0))
                stringbuilder.append(',')
                stringbuilder.append(mylist[3+i])
                stringbuilder.append(',')
        fw.write(''.join(stringbuilder))
fr.close()
fw.close()
