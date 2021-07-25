import os
DEV_PATH="../mnt"
RESULT_PATH="../result_txt"
NUM=5000000
RESULT_FILE="test7_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.txt"
NAME="test7_report_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
key_vars=[16,32,64,128,256,1024]
value_vars=[64,128,256,512,1024,4096]
compactionstyle=[0,1]
benchmark=["fillrandom","readrandom"]
I=0
bench=""
PARSER="../python_parser"
PARSER_RESULT="test7_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
PARSER_RESULT2="test7_99_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
PARSER_RESULT3="test7_avg_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"



RESULT_FILE="test7_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.txt"


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

                RESULT_FILE="test7_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.txt"
                PARSER_RESULT="test7_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
                PARSER_RESULT2="test7_99_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
                PARSER_RESULT3="test7_avg_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"


print("*********** parser FIN ***************")
