# Python parser for Latency evaluation

import sys
import re

file_path_r = sys.argv[1]
file_path_w = sys.argv[2]

fr = open(file_path_r, 'r')
fw = open(file_path_w, 'w')

#_pattern = '^[0-9]{5,}' # == '^\d{5,}'
_init_pattern = '^=+'
_pattern = '^(\d{8})(\d{2})(\d{3})(\d{3})'  #1. 시간~분 2.초 3.밀리초ms 4.마이크로초us 

_init = re.compile(_init_pattern)
_parser = re.compile(_pattern)
__parser = re.compile('start|end')

line = None
start_sec = None
index=0
fw.write("time,level0,level1,level2,level3,level4,level5,level6\n")
#print("time,level0,level1,level2,level3,level4,level5,level6")

while line != '':
   line = fr.readline()
   mylist = line.split(' ')
   if _init.match(mylist[0]) != None :
       fw.write(''.join(mylist))
       continue
   if len(mylist)>1 and __parser.match(mylist[1])!=None:
       fw.write('{0},0,0,0,0,0,0,0\n'.format(int(mylist[3])))
   if _parser.match(mylist[0]) != None: 
       #then we found match object 
       stringbuilder = []
       stringbuilder.append(mylist[0]) #us
       stringbuilder.append(',')
       for i in range(7):
           stringbuilder.append(mylist[4+i])
           stringbuilder.append(',')
       stringbuilder[-1] = '\n'
       fw.write(''.join(stringbuilder))
       #print(''.join(stringbuilder))
       # us 차이 출력

fr.close()
fw.close()
