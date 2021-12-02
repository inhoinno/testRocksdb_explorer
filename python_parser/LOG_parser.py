import re
import os
import sys
file_path_r = sys.argv[1]
file_path_w = sys.argv[2]
fr=open(file_path_r, 'r')
fw=open(file_path_w, 'w')
stack=[]
mb=0
count=0

_pattern ='Compaction start summary'
line=None
fw.write('time, Base level, L0, L0_num, L1, L1_num, L2, L2_num, L3, L3_num, L4, L4_num, L5, L5_num, L6 , L6_num\n')
#16 columns
while line != '':
    line = fr.readline()
    if re.search(_pattern,line) != None:
        if re.search('\d',line) != None:
            #print(line)
            mylist = line.split(' ')
            fw.write(''.join(mylist[0]))
            fw.write(',')
            fw.write(''.join(mylist[12].replace(',','')))
            fw.write(',')
            bracket_ = mylist[14:]
            bracket_list=' '.join(bracket_)
            print(bracket_list.replace('MB',''))
            bracket_list = bracket_list.replace('MB', '')
            for i in range(len(bracket_list)):
                if (bracket_list[i] == '[') :
                    stack.append(i)
                elif (bracket_list[i]=='(') :
                    stack.append(i)
                elif (bracket_list[i] == ')') :
                    #add mb += int(str(stack[-1] to i))  #print(stack[-1],i)
                    if re.search('KB',bracket_list[stack[-1]+1 : i]) != None:
                        mb+=float(bracket_list[stack[-1]+1 : i].replace('KB',''))/1024
                    else : 
                        mb += float(bracket_list[stack[-1]+1:i]) # MB
                    #add count += 1
                    count+=1
                    stack.pop()
                elif (bracket_list[i] == ']') :
                    #level done
                    stack.pop()
                    fw.write(str(mb))
                    fw.write(',')
                    fw.write(str(count))
                    fw.write(',')
                    mb = 0
                    count = 0
            fw.write('\n')
fr.close()
fw.close()
