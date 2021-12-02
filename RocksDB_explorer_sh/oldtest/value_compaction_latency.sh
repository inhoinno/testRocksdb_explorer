#!/bin/bash

DEV_PATH=$1
RESULT_PATH="../result_txt/"
VALUE_SIZE=512
NUM=20000000
BENCHMARK=fillrandom,levelstats,stats,sstables

print > $RESULT_PATH/compaction_on_latency_result.txt
echo ========== Operation Compaction on for Latency =========== >> $RESULT_PATH/compaction_on_latency_result.txt 
../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --histogram --value_size=$VALUE_SIZE --num=$NUM --disable_auto_compactions=false --level0_file_num_compaction_trigger=-1 --statistics>> $RESULT_PATH/compaction_on_latency_result.txt

VALUE_SIZE=1024

print > $RESULT_PATH/compaction_on2_latency_result.txt
echo ========== Operation Compaction off for Latency =========== >> $RESULT_PATH/compaction_off_latency_result.txt
../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --histogram --value_size=$VALUE_SIZE --num=$NUM --disable_auto_compactions=false --level0_file_num_compaction_trigger=-1 --statistics>> $RESULT_PATH/compaction_on2_latency_result.txt
