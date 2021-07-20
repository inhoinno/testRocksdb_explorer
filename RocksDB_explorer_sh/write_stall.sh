DEV_PATH=$1
RESULT_PATH="../result_txt"
VALUE_SIZE=512
NUM=50
#   5000000     5       mil
#   10000000    10      mil
#   50000000    50      mil
#   100000000   100     mil
#   1000000000  1       bil
BENCHMARK=fillrandom,levelstats
MEM_NUM=4
let MEM_SIZE=64*1024*1024
RESULT_FILE="write_stall.txt"
print > $RESULT_PATH/$RESULT_FILE
echo ========== $BENCHMARK] Test1 MemTable size Compaction Latency =========== >> $RESULT_PATH/$RESULT_FILE
../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --histogram --value_size=$VALUE_SIZE --num=$NUM --disable_auto_compactions=false --level0_file_num_compaction_trigger=-1 --write_buffer_size=$MEM_SIZE >> $RESULT_PATH/$RESULT_FILE

