import os
import re
import sys
file_path_r = sys.argv[1]
file_path_w = sys.argv[2]
fr=open(file_path_r)
fw=open(file_path_w)

_pattern='Comapction start summary'
line = None
while line != '':
    line = fr.readline()
    if re.search(_pattern, line) != None:
        mylist = line.split(' ')
        mylist = mylist[3:]

           
