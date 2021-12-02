import os
from collections import defaultdict
DEV_PATH="../mnt"
RESULT_PATH="../result_txt"
NUM= 25000000 # ~10GB
#UM= 55000000 #~25GB
#UM=110000000  #~50GB
#UM=210000000  #100.13GB
#UM=1250000000 #596.04GB
RESULT_FILE="test16_readamp_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.txt"
NAME="test16_report_readamp_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv"
key_vars=[16]#,32,64,128,256,1024]
value_vars=[128,256,512,1024,4096]
cache_vars=[512,1024,2048] 
target_num = (256+256)*NUM

d = defaultdict(dict)
for k in key_vars:
    for v in value_vars:
        d[k][v] = int(target_num/(k+v))
        #print(k,v,target_num/(k+v))
#print(d[256][256])

compactionstyle=[0,1]
benchmark=["fillseq","seekrandom"]
I=0
bench=""

for i in compactionstyle:
    for k in key_vars:
        for v in value_vars:
            for c in cache_vars:
                for b in benchmark:
                    BENCHMARK="{0},levelstats,stats".format(b)
                    if i == 0 :
                        RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","LVL")
                        NAME = NAME.replace("COMPACTIONSTYLE","LVL")
                    elif i == 1 :
                        RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","UNIV")
                        NAME=NAME.replace("COMPACTIONSTYLE","UNIV")
                    RESULT_FILE = RESULT_FILE.replace("BENCH",b) 
                    RESULT_FILE = RESULT_FILE.replace("KEY",str(k))
                    RESULT_FILE = RESULT_FILE.replace("VALUE",str(v))
                    RESULT_FILE = RESULT_FILE.replace("BLOCKCACHE",str(c))
                    NAME = NAME.replace("BENCH",b) 
                    NAME = NAME.replace("KEY",str(k))
                    NAME = NAME.replace("VALUE",str(v))
                    NAME = NAME.replace("BLOCKCACHE",str(c))
                    c = int(c*1024*1024)
                    if (b == "readrandom") | (b=="readseq") | (b=="seekrandom"):
                        bench = "../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --key_size=$k --value_size=$v --num=$NUM --compaction_style=$COMPACTIONSTYLE --use_existing_db=true --prefix_size=14 --keys_per_prefix=8 --readonly=true --histogram --statistics --cache_size=$c --read_amp_bytes_per_bit=16 --report_interval_seconds=1 --report_file=$RESULT_PATH/$NAME >> $RESULT_PATH/$RESULT_FILE"
                    elif (b == "fillrandom") | (b=="fillseq"): 
                        bench = "../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --key_size=$k --value_size=$v --num=$NUM --compaction_style=$COMPACTIONSTYLE --histogram --statistics --cache_size=$c --prefix_size=14 --keys_per_prefix=8 --read_amp_bytes_per_bit=16  --report_interval_seconds=1 --report_file=$RESULT_PATH/$NAME >> $RESULT_PATH/$RESULT_FILE"

                    bench = bench.replace("$DEV_PATH",DEV_PATH).replace("$BENCHMARK",BENCHMARK).replace("$k",str(k),2).replace("$v",str(v),2).replace("$NUM",str(d[k][v])).replace("$COMPACTIONSTYLE",str(i)).replace("$NAME",NAME).replace("$RESULT_PATH", RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE).replace("$c",str(c))
                    #print(bench)
                    os.system("print > {0}/{1}".format(RESULT_PATH,RESULT_FILE))
                    os.system("echo =========== {0} Compaction Style = {1} key size = {2}, value size = {3}, block cache size = {4} =========== >>{5}/{6}".format(b,i,k,v,c,RESULT_PATH,RESULT_FILE))
                    os.system(bench)
                    #print(I, RESULT_PATH+'/'+RESULT_FILE)
                    RESULT_FILE="test16_readamp_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.txt"
                    NAME="test16_readamp_report_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv"
                    c /= 1024*1024
                    c = int(c)
                    I+=1


print("*********** bench FIN ****************")
PARSER="../python_parser"
PARSER_RESULT="test16_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv"
PARSER_RESULT2="test16_99_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv"
PARSER_RESULT3="test16_avg_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv"
PARSER_RESULT4="test16_statistics_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv"


RESULT_FILE="test16_readamp_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.txt"


for i in compactionstyle:
    for k in key_vars:
        for v in value_vars:
            for c in cache_vars:
                for b in benchmark:
                    BENCHMARK="{0},levelstats,stats".format(b)

                    if i == 0 :
                        PARSER_RESULT = PARSER_RESULT.replace("COMPACTIONSTYLE","LVL")
                        PARSER_RESULT2 = PARSER_RESULT2.replace("COMPACTIONSTYLE","LVL")
                        PARSER_RESULT3 = PARSER_RESULT3.replace("COMPACTIONSTYLE","LVL")
                        PARSER_RESULT4 = PARSER_RESULT4.replace("COMPACTIONSTYLE","LVL")
                        RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","LVL")
                    elif i==1 :
                        PARSER_RESULT = PARSER_RESULT.replace("COMPACTIONSTYLE","UNIV")
                        PARSER_RESULT2 = PARSER_RESULT2.replace("COMPACTIONSTYLE","UNIV")
                        PARSER_RESULT3 = PARSER_RESULT3.replace("COMPACTIONSTYLE","UNIV")
                        PARSER_RESULT4 = PARSER_RESULT4.replace("COMPACTIONSTYLE","UNIV")
                        RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","UNIV")

                    RESULT_FILE = RESULT_FILE.replace("KEY",str(k))
                    RESULT_FILE = RESULT_FILE.replace("VALUE",str(v))
                    RESULT_FILE = RESULT_FILE.replace("BLOCKCACHE",str(c))
                    
                    PARSER_RESULT = PARSER_RESULT.replace("KEY",str(k))
                    PARSER_RESULT = PARSER_RESULT.replace("VALUE",str(v))
                    PARSER_RESULT = PARSER_RESULT.replace("BLOCKCACHE",str(c))
                    
                    PARSER_RESULT2 = PARSER_RESULT2.replace("KEY",str(k))
                    PARSER_RESULT2 = PARSER_RESULT2.replace("VALUE",str(v))
                    PARSER_RESULT2 = PARSER_RESULT2.replace("BLOCKCACHE",str(c))
                    
                    PARSER_RESULT3 = PARSER_RESULT3.replace("KEY",str(k))
                    PARSER_RESULT3 = PARSER_RESULT3.replace("VALUE",str(v))
                    PARSER_RESULT3 = PARSER_RESULT3.replace("BLOCKCACHE",str(c))
                    
                    PARSER_RESULT4 = PARSER_RESULT4.replace("KEY",str(k))
                    PARSER_RESULT4 = PARSER_RESULT4.replace("VALUE",str(v))
                    PARSER_RESULT4 = PARSER_RESULT4.replace("BLOCKCACHE",str(c))
                    
                    RESULT_FILE = RESULT_FILE.replace("BENCH",b)
                    PARSER_RESULT = PARSER_RESULT.replace("BENCH",b)
                    PARSER_RESULT2 = PARSER_RESULT2.replace("BENCH",b)
                    PARSER_RESULT3 = PARSER_RESULT3.replace("BENCH",b)
                    PARSER_RESULT4 = PARSER_RESULT3.replace("BENCH",b)



                    compaction_parser="python3 $PARSER/compaction_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                    latency_parser="python3 $PARSER/99parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                    avg_perf_parser="python3 $PARSER/{0}_averagePerformance_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT".format(b)
                    statistics_parser="python3 $PARSER/statistics_context_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                    
                    compaction_parser=compaction_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT)
                    latency_parser=latency_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT2)
                    avg_perf_parser=avg_perf_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT3)
                    statistics_parser=statistics_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT4)
                    os.system(compaction_parser)
                    os.system(latency_parser)
                    os.system(avg_perf_parser)
                    os.system(statistics_parser)
                    #print(compaction_parser)
                    #print(latency_parser)
                    #print(avg_perf_parser)

                    RESULT_FILE="test16_readamp_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.txt"
                    PARSER_RESULT="test16_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv"
                    PARSER_RESULT2="test16_99_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv"
                    PARSER_RESULT3="test16_avg_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv"
                    PARSER_RESULT4="test16_statistics_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv"

print("*********** parser FIN ***************")

