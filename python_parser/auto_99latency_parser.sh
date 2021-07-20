#!/bin/bash

for i in {4..5};
do

   let k=$((2**($i+1)))
   v="various_memtable_64SSTable.txt"
   python3 99parser.py ../result_txt/test5_$k$v ./csv/test5_99lat$k.csv

done

