# Python parser for Latency evaluation

import sys
import re
file_path_r = sys.argv[1]
file_path_w = sys.argv[2]

fr = open(file_path_r, 'r')
fw = open(file_path_w, 'w')

_parser = 'Latency'
_init_pattern='^=+'
_init=re.compile(_init_pattern)
line = None
while line != '':
   line = fr.readline()

   mylist = line.split(' ')
   if _init.match(mylist[0]):
       fw.write(''.join(mylist))
                    
   if mylist[0] == _parser:
       fw.write(mylist[5])

fr.close()
fw.close()
