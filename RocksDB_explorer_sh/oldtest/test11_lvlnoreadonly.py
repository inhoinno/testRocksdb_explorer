import os
DEV_PATH="../mnt"
RESULT_PATH="../result_txt"
NUM= 55000000  #~25GB

RESULT_FILE="test11_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.txt"
NAME="test11_report_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
key_vars=[16]#]
value_vars=[128]#,256,512,1024,4096]
compactionstyle=[0,1]
benchmark=["fillrandom","readrandom"]
I=0
bench=""
for i in compactionstyle:
    for k in key_vars:
        for v in value_vars:
            for b in benchmark:
                BENCHMARK="{0},levelstats,stats".format(b)
                if i == 0 :
                    RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","LVL")
                    NAME = NAME.replace("COMPACTIONSTYLE","LVL")
                elif i==1 :
                    RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","UNIV")
                    NAME=NAME.replace("COMPACTIONSTYLE","UNIV")
                RESULT_FILE = RESULT_FILE.replace("BENCH",b) 
                RESULT_FILE = RESULT_FILE.replace("KEY",str(k))
                RESULT_FILE = RESULT_FILE.replace("VALUE",str(v))
                NAME = NAME.replace("BENCH",b) 
                NAME = NAME.replace("KEY",str(k))
                NAME = NAME.replace("VALUE",str(v))

                if b == "readrandom":
                    #RESULT_FILE = RESULT_FILE.replace("BENCH","readrandom")
                    #NAME = NAME.replace("BENCH","readrandom")
                    bench = "../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --key_size=$k --value_size=$v --num=$NUM --compaction_style=$COMPACTIONSTYLE --use_existing_db=true --readonly=false --histogram --statistics  --report_interval_seconds=1 --report_file=$RESULT_PATH/$NAME >> $RESULT_PATH/$RESULT_FILE"
                elif b == "fillrandom": 
                    #RESULT_FILE = RESULT_FILE.replace("BENCH","fillrandom")
                    #NAME = NAME.replace("BENCH","fillrandom")
                    bench = "../db_bench --db=$DEV_PATH --use_direct_io_for_flush_and_compaction=true --benchmarks=$BENCHMARK --key_size=$k --value_size=$v --num=$NUM --compaction_style=$COMPACTIONSTYLE --histogram --statistics  --report_interval_seconds=1 --report_file=$RESULT_PATH/$NAME >> $RESULT_PATH/$RESULT_FILE"

                bench = bench.replace("$DEV_PATH",DEV_PATH).replace("$BENCHMARK",BENCHMARK).replace("$k",str(k),2).replace("$v",str(v),2).replace("$NUM",str(NUM)).replace("$COMPACTIONSTYLE",str(i)).replace("$NAME",NAME).replace("$RESULT_PATH", RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE)
                #print(bench)
                os.system("print > {0}/{1}".format(RESULT_PATH,RESULT_FILE))
                os.system("echo =========== {0} Compaction Style = {1} key size = {2}, value size = {3} =========== >>{4}/{5}".format(b,i,k,v,RESULT_PATH,RESULT_FILE))
                os.system(bench)
                #print(I, RESULT_PATH+'/'+RESULT_FILE)
                RESULT_FILE="test11_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.txt"
                NAME="test11_report_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"

                I+=1


print("*********** bench FIN ****************")
PARSER="../python_parser"
PARSER_RESULT="test11_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
PARSER_RESULT2="test11_99_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
PARSER_RESULT3="test11_avg_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"



RESULT_FILE="test11_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.txt"


for i in compactionstyle:
    for k in key_vars:
        for v in value_vars:
            for b in benchmark:
                BENCHMARK="{0},levelstats,stats".format(b)
                
                if i == 0 :
                    PARSER_RESULT = PARSER_RESULT.replace("COMPACTIONSTYLE","LVL")
                    PARSER_RESULT2 = PARSER_RESULT2.replace("COMPACTIONSTYLE","LVL")
                    PARSER_RESULT3 = PARSER_RESULT3.replace("COMPACTIONSTYLE","LVL")
                    RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","LVL")
                elif i==1 :
                    PARSER_RESULT = PARSER_RESULT.replace("COMPACTIONSTYLE","UNIV")
                    PARSER_RESULT2 = PARSER_RESULT2.replace("COMPACTIONSTYLE","UNIV")
                    PARSER_RESULT3 = PARSER_RESULT3.replace("COMPACTIONSTYLE","UNIV")
                    RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","UNIV")

                RESULT_FILE = RESULT_FILE.replace("KEY",str(k))
                RESULT_FILE = RESULT_FILE.replace("VALUE",str(v))

                PARSER_RESULT = PARSER_RESULT.replace("KEY",str(k))
                PARSER_RESULT = PARSER_RESULT.replace("VALUE",str(v))
                PARSER_RESULT2 = PARSER_RESULT2.replace("KEY",str(k))
                PARSER_RESULT2 = PARSER_RESULT2.replace("VALUE",str(v))
                PARSER_RESULT3 = PARSER_RESULT3.replace("KEY",str(k))
                PARSER_RESULT3 = PARSER_RESULT3.replace("VALUE",str(v))

                RESULT_FILE = RESULT_FILE.replace("BENCH",b)
                PARSER_RESULT = PARSER_RESULT.replace("BENCH",b)
                PARSER_RESULT2 = PARSER_RESULT2.replace("BENCH",b)
                PARSER_RESULT3 = PARSER_RESULT3.replace("BENCH",b)



                compaction_parser="python3 $PARSER/compaction_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                latency_parser="python3 $PARSER/99parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                avg_perf_parser="python3 $PARSER/{0}_averagePerformance_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT".format(b)
                
                compaction_parser=compaction_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT)

                latency_parser=latency_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT2)
                avg_perf_parser=avg_perf_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT3)

                os.system(compaction_parser)
                os.system(latency_parser)
                os.system(avg_perf_parser)
                #print(compaction_parser)
                #print(latency_parser)
                #print(avg_perf_parser)

                RESULT_FILE="test11_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.txt"
                PARSER_RESULT="test11_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
                PARSER_RESULT2="test11_99_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
                PARSER_RESULT3="test11_avg_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"


print("*********** parser FIN ***************")
