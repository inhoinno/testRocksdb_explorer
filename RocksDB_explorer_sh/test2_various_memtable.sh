#!/bin/bash

DEV_PATH=$1
RESULT_PATH="../result_txt"
VALUE_SIZE=512
NUM=10000000
#   5000000 	5	mil
#   10000000 	10	mil
#   50000000	50	mil
#   100000000	100	mil
#   1000000000	1	bil
BENCHMARK=fillrandom,levelstats
L0_FILE_NUM=-1
let MEM_SIZE=64*1024*1024
RESULT_FILE="test2_64various_memtable.txt"

print > $RESULT_PATH/$RESULT_FILE
echo ========== fillrandom 64MB] Test2 MemTable size Compaction Latency =========== >> $RESULT_PATH/$RESULT_FILE
../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --histogram --value_size=$VALUE_SIZE --num=$NUM --disable_auto_compactions=false --level0_file_num_compaction_trigger=$L0_FILE_NUM --write_buffer_size=$MEM_SIZE --target_file_size_base=$MEM_SIZE >> $RESULT_PATH/$RESULT_FILE

let MEM_SIZE=32*1024*1024
MEM_NUM=4
RESULT_FILE="test2_32various_memtable.txt"

print > $RESULT_PATH/$RESULT_FILE
echo ========== fillrandom 32MB] Test2 MemTable size Compaction Latency =========== >> $RESULT_PATH/$RESULT_FILE
../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --histogram --value_size=$VALUE_SIZE --num=$NUM --disable_auto_compactions=false --level0_file_num_compaction_trigger=$L0_FILE_NUM --write_buffer_size=$MEM_SIZE --max_write_buffer_number=$MEM_NUM --target_file_size_base=$MEM_SIZE >> $RESULT_PATH/$RESULT_FILE

let MEM_SIZE=16*1024*1024
MEM_NUM=8
RESULT_FILE="test2_16various_memtable.txt"

print > $RESULT_PATH/$RESULT_FILE
echo ========== fillrandom 16MB] Test2 MemTable size Compaction Latency =========== >> $RESULT_PATH/$RESULT_FILE
../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --histogram --value_size=$VALUE_SIZE --num=$NUM --disable_auto_compactions=false --level0_file_num_compaction_trigger=$L0_FILE_NUM --write_buffer_size=$MEM_SIZE --max_write_buffer_number=$MEM_NUM --target_file_size_base=$MEM_SIZE >> $RESULT_PATH/$RESULT_FILE

#let MEM_SIZE=8*1024*1024
#MEM_NUM=16
#RESULT_FILE="test2_8various_memtable.txt"

#print > $RESULT_PATH/$RESULT_FILE
#echo ========== fillrandom 8MB] Test2 MemTable size Compaction Latency =========== >> $RESULT_PATH/$RESULT_FILE
#../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --histogram --value_size=$VALUE_SIZE --num=$NUM --disable_auto_compactions=false --level0_file_num_compaction_trigger=$L0_FILE_NUM --write_buffer_size=$MEM_SIZE --max_write_buffer_number=$MEM_NUM --target_file_size_base=$MEM_SIZE >> $RESULT_PATH/$RESULT_FILE

#let MEM_SIZE=4*1024*1024
#MEM_NUM=32
#RESULT_FILE="test2_4various_memtable.txt"

#print > $RESULT_PATH/$RESULT_FILE
#echo ========== fillrandom 4MB] Test2 MemTable size Compaction Latency =========== >> $RESULT_PATH/$RESULT_FILE
#../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --histogram --value_size=$VALUE_SIZE --num=$NUM --disable_auto_compactions=false --level0_file_num_compaction_trigger=$L0_FILE_NUM --write_buffer_size=$MEM_SIZE --max_write_buffer_number=$MEM_NUM --target_file_size_base=$MEM_SIZE >> $RESULT_PATH/$RESULT_FILE

#let MEM_SIZE=2*1024*1024
#MEM_NUM=64
#RESULT_FILE="test2_2various_memtable.txt"


#print > $RESULT_PATH/$RESULT_FILE
#echo ========== fillrandom 2MB] Test2 MemTable size Compaction Latency =========== >> $RESULT_PATH/$RESULT_FILE
#../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --histogram --value_size=$VALUE_SIZE --num=$NUM --disable_auto_compactions=false --level0_file_num_compaction_trigger=$L0_FILE_NUM --write_buffer_size=$MEM_SIZE --max_write_buffer_number=$MEM_NUM --target_file_size_base=$MEM_SIZE >> $RESULT_PATH/$RESULT_FILE




