#!/bin/bash

DEV_PATH="../mnt"
RESULT_PATH="../result_txt/"
NUM=500
BENCHMARK=fillrandom,levelstats,stats
RESULT_FILE="small_fillrandom_key"
RESULT_FILE2="small_readrandom_key"
R="_value"

key_vars=(16)
value_vars=(256)

for k in ${key_vars[@]};
do 
    for v in ${value_vars[@]};
    do 
        BENCHMARK=fillrandom,levelstats,stats
        #bench1 : fillrandom
        #Result File : "test6_fillrandom_key_value.txt" 
        print > $RESULT_PATH/$RESULT_FILE$k$R$v.txt
        echo ==========fillrandom] key size = $k, value size = $v =========== >> $RESULT_PATH/$RESULT_FILE$k$R$v.txt
        ../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --key_size=$k --value_size=$v --num=$NUM --histogram >> $RESULT_PATH/$RESULT_FILE$k$R$v.txt
        BENCHMARK=readrandom,levelstats,stats
        #bench2 : readrandom
        #Result File : "test6_readrandom_key_value.txt"
        print > $RESULT_PATH/$RESULT_FILE2$k$R$v.txt
        echo ==========readrandom] key size = $k, value size = $v =========== >> $RESULT_PATH/$RESULT_FILE2$k$R$v.txt
        ../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --key_size=$k --value_size=$v --num=$NUM --use_existing_db --histogram >> $RESULT_PATH/$RESULT_FILE2$k$R$v.txt

    done 
done

echo "********* Bench Fin *********"
