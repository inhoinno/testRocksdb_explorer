# Python parser for Latency evaluation

import sys
import re
import numpy as np
file_path_r = sys.argv[1]
file_path_w = sys.argv[2]

fr = open(file_path_r, 'r')
fw = open(file_path_w, 'w')

_parser = 'Percentiles:'
_init_pattern='^=+'
_init=re.compile(_init_pattern)

_pattern='\d\d.\d\d|\d\d.\d+|\d\d+'
__parser=re.compile(_pattern)

line = None
counter =0
while line != '':
   line = fr.readline()
   mylist = line.split(' ')
   if _init.match(mylist[0])!=None and counter==0:
       fw.write(''.join(mylist))
   if mylist[0] == _parser:
       stringbuilder=[]
       for i in np.arange(0,len(mylist[1:]),2):
           stringbuilder.append(__parser.search(mylist[1+i]).group(0))
           stringbuilder.append(',')
           stringbuilder.append(mylist[2+i])
           stringbuilder.append('\n')
       fw.write(''.join(stringbuilder))
       #print(''.join(stringbuilder))

fr.close()
fw.close()
