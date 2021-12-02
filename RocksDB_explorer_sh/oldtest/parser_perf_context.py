#perf context parser script
import os
DEV_PATH="../mnt"
RESULT_PATH="../result_txt"
#NUM=5000000
RESULT_FILE="test9_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cCACHE.txt"
#NAME="test7_report_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
key_vars=[16,32,64,128,256,1024]
value_vars=[64,128,256,512,1024,4096]
#cache_vars=[8,16,32,64,256]
compactionstyle=[0,1]
benchmark=["fillrandom","readrandom"]
#I=0
bench=""
PARSER="../python_parser"
PARSER_RESULT3="test9_perf_context_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"#_cCACHE.csv"
OLD_PARSER_RESULT3="test9_perf_context_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
#PARSER_RESULT2="test7_99_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"
#PARSER_RESULT3="test7_avg_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.csv"



RESULT_FILE="test9_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.txt"#_cCACHE.txt"
OLD_RESULT_FILE = "test9_COMPACTIONSTYLE_BENCH_kKEY_vVALUE.txt"

for i in compactionstyle:
    for k in key_vars:
        for v in value_vars:
            for b in benchmark:
                #for c in cache_vars:
                #BENCHMARK="{0},levelstats,stats".format(b) 
                if i == 0 :
                    PARSER_RESULT3 = PARSER_RESULT3.replace("COMPACTIONSTYLE","LVL")
                    RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","LVL")
                elif i==1 :
                    PARSER_RESULT3 = PARSER_RESULT3.replace("COMPACTIONSTYLE","UNIV")
                    RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","UNIV")

                RESULT_FILE = RESULT_FILE.replace("KEY",str(k))
                RESULT_FILE = RESULT_FILE.replace("VALUE",str(v))

                PARSER_RESULT3 = PARSER_RESULT3.replace("KEY",str(k))
                PARSER_RESULT3 = PARSER_RESULT3.replace("VALUE",str(v))

                RESULT_FILE = RESULT_FILE.replace("BENCH",b)
                PARSER_RESULT3 = PARSER_RESULT3.replace("BENCH",b)
                
                #RESULT_FILE = RESULT_FILE.replace("CACHE",str(c))
                #PARSER_RESULT3 = PARSER_RESULT3.replace("CACHE",str(c))



                perf_context_parser="python3 $PARSER/perf_context_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                
                perf_context_parser=perf_context_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT3)

                #os.system(avg_perf_parser)
                #print(compaction_parser)
                #print(latency_parser)
                os.system(perf_context_parser)


                RESULT_FILE=OLD_RESULT_FILE 
                PARSER_RESULT3=OLD_PARSER_RESULT3


print("*********** parser 	 FIN ***************")
