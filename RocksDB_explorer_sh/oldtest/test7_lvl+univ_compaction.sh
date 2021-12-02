#!/bin/bash


EV_PATH="../mnt"
RESULT_PATH="../result_txt"
NUM=5000000
BENCHMARK=fillrandom,levelstats,stats
RESULT_FILE="test7_COMPACTIONSTYLE_BENCH_kKEY_vVALUE"
RESULT_FILE2="test7_readrandom_key"
R="_value"
S=".csv"
NAME="report"
key_vars=(16 32 64 128 256 1024)
value_vars=(256 512 1024 4096)

for k in ${key_vars[@]};
do 
    for v in ${value_vars[@]};
    do 
        BENCHMARK=fillrandom,levelstats,stats
        NAME=$RESULT_FILE$k$R$vi.csv
        #bench1 : fillrandom
        #Result File : "test7_fillrandom_key_value.txt" 
        print > $RESULT_PATH/$RESULT_FILE$k$R$v.txt
        echo ==========fillrandom] key size = $k, value size = $v =========== >> $RESULT_PATH/$RESULT_FILE$k$R$v.txt
        ../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --key_size=$k --value_size=$v --num=$NUM --compaction_style=1 --histogram --statistics  --report_interval_seconds=1 --report_file=$NAME >> $RESULT_PATH/$RESULT_FILE$k$R$v.txt
        BENCHMARK=readrandom,levelstats,stats
        NAME=$RESULT_FILE2$k$R$v.csv
        #bench2 : readrandom
        #Result File : "test7_readrandom_key_value.txt"
        print > $RESULT_PATH/$RESULT_FILE2$k$R$v.txt
        echo ==========readrandom] key size = $k, value size = $v =========== >> $RESULT_PATH/$RESULT_FILE2$k$R$v.txt
        ../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --key_size=$k --value_size=$v --num=$NUM --compaction_style=1 --histogram --statistics --use_existing_db=true --readonly=true --report_interval_seconds=1 --report_file=$NAME >> $RESULT_PATH/$RESULT_FILE2$k$R$v.txt

    done 
done

echo "********** Bench Fin **********"

i="_v" 
PARSER="../python_parser"
for k in ${key_vars[@]};
do
    for v in ${value_vars[@]};
    do
        python3 $PARSER/compaction_parser.py $RESULT_PATH/$RESULT_FILE$k$R$v.txt $PARSER/csv/universal_test/test7_k$k$i$v.csv
        python3 $PARSER/compaction_parser.py $RESULT_PATH/$RESULT_FILE2$k$R$v.txt $PARSER/csv/universal_test/test7-2_k$k$i$v.csv
        python3 $PARSER/99parser.py $RESULT_PATH/$RESULT_FILE$k$R$v.txt $PARSER/csv/universal_test/test7_99_k$k$i$v.csv
        python3 $PARSER/99parser.py $RESULT_PATH/$RESULT_FILE2$k$R$v.txt $PARSER/csv/universal_test/test7-2_99_k$k$i$v.csv
        python3 $PARSER/fillrandom_averagePerformance_parser.py $RESULT_PATH/$RESULT_FILE$k$R$v.txt $PARSER/csv/universal_test/test7_k$k$i$v.csv
        python3 $PARSER/fillrandom_averagePerformance_parser.py $RESULT_PATH/$RESULT_FILE2$k$R$v.txt $PARSER/csv/universal_test/test7-2_k$k$i$v.csv
    done
done

echo "********* parser Fin ***********"

