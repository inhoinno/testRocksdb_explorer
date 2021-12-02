# Python parser for Latency evaluation

import sys
import re
import numpy as np
file_path_r = sys.argv[1]
file_path_w = sys.argv[2]

fr = open(file_path_r, 'r')
fw = open(file_path_w, 'w')

_init_pattern='^=+'
_init=re.compile(_init_pattern)

_pattern='\s+L0|\s+L1|\s+L2|\s+L3|\s+L4|\s+L5|\s+L6|\s+Sum'
__parser=re.compile(_pattern)

line = None
counter =0
while line != '':
   line = fr.readline()
   mylist = line.split(' ')
   if mylist[0]=='Level' and mylist[1]=='':
       mylist=re.split(r'\s+',' '.join(mylist))
       #print(mylist)
       mylist[-1] = '\n'
       fw.write(','.join(mylist))
   if __parser.match(line) != None:
       #stringbuilder=[]
       #for i in np.arange(0,len(mylist[1:]),2):
       #stringbuilder.append(__parser.search(mylist[1+i]).group(0))
       #stringbuilder.append(',')
       #stringbuilder.append(mylist[2+i])
       #stringbuilder.append('\n')
       #fw.write(','.join(mylist))
       mylist=re.split(r'\s+',' '.join(mylist))
       mylist=mylist[1:]
       if mylist[3] == 'GB':
           mylist[2] = str(float(mylist[2])*1024)
       elif mylist[3] == 'TB':
           mylist[2] = str(float(mylist[2])*1024*1024)
       del mylist[3]
       mylist.append('\n')
       #print(','.join(mylist))
       fw.write(','.join(mylist))

fr.close()
fw.close()
