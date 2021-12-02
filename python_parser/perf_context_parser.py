# Python parser for Latency evaluation

import sys
import re
import numpy as np
file_path_r = sys.argv[1]
file_path_w = sys.argv[2]

fr = open(file_path_r, 'r')
fw = open(file_path_w, 'w')

_parser = re.compile(' PERF_')
#_init_pattern='^=+'
#_init=re.compile(_init_pattern)

#_pattern='\d\d.\d\d|\d\d.\d+|\d\d+'
#__parser=re.compile(_pattern)

line = None
counter =0
while line != '':
   line = fr.readline()
   mylist = line.split(' ')
   if _parser.search(line) != None:
       line=fr.readline()
       mylist=line.split(',')
       #stringbuilder=[]
       fw.write('\n'.join([x.replace(' = ',',') for x in mylist]))

fr.close()
fw.close()
