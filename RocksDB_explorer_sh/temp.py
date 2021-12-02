import os
from collections import defaultdict
DEV_PATH="../mnt"
RESULT_PATH="../result_txt"

testname = "uniformtest17_Fig1"


NUM= 25000000 # ~10GB
#UM= 55000000 #~25GB
#UM=110000000  #~50GB
#UM=210000000  #100.13GB
#UM=1250000000 #596.04GB
RESULT_FILE="{0}_readamp_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.txt".format(testname)
OLDRESULT_FILE = RESULT_FILE

NAME="{0}_report_readamp_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv".format(testname)
OLDNAME=NAME

key_vars=[16]#,32,64,128,256,1024]
value_vars=[64]#,64,128,256,512,1024,4096]
cache_vars=[512,1024,2048] 
#target_num = (256+256)*NUM

#d = defaultdict(dict)
#for k in key_vars:
    #for v in value_vars:
        #d[k][v] = int(target_num/(k+v))
        #print(k,v,target_num/(k+v))
#print(d[256][256])

compactionstyle=[0,1]
benchmark=["fillrandom","readrandom"]
I=0
bench=""

PARSER="../python_parser"
PARSER_RESULT1="{0}_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv".format(testname)
PARSER_RESULT2="{0}_99_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv".format(testname)
PARSER_RESULT3="{0}_avg_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv".format(testname)
PARSER_RESULT4="{0}_statistics_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv".format(testname)
PARSER_RESULT5="{0}_perf_context_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE.csv".format(testname)

OLD1=PARSER_RESULT1
OLD2=PARSER_RESULT2
OLD3=PARSER_RESULT3
OLD4=PARSER_RESULT4
OLD5=PARSER_RESULT5

RESULT_FILE=OLDRESULT_FILE

PARSER_RESULTS = [RESULT_FILE, PARSER_RESULT1, PARSER_RESULT2, PARSER_RESULT3, PARSER_RESULT4, PARSER_RESULT5]


for i in compactionstyle:
    for k in key_vars:
        for v in value_vars:
            for c in cache_vars:
                for b in benchmark:
                    BENCHMARK="{0},levelstats,stats".format(b)

                    if i == 0 :
                        PARSER_RESULT1 = PARSER_RESULT1.replace("COMPACTIONSTYLE","LVL")
                        PARSER_RESULT2 = PARSER_RESULT2.replace("COMPACTIONSTYLE","LVL")
                        PARSER_RESULT3 = PARSER_RESULT3.replace("COMPACTIONSTYLE","LVL")
                        PARSER_RESULT4 = PARSER_RESULT4.replace("COMPACTIONSTYLE","LVL")
                        PARSER_RESULT5 = PARSER_RESULT5.replace("COMPACTIONSTYLE","LVL")
                        RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","LVL")
                    elif i==1 :
                        PARSER_RESULT1 = PARSER_RESULT1.replace("COMPACTIONSTYLE","UNIV")
                        PARSER_RESULT2 = PARSER_RESULT2.replace("COMPACTIONSTYLE","UNIV")
                        PARSER_RESULT3 = PARSER_RESULT3.replace("COMPACTIONSTYLE","UNIV")
                        PARSER_RESULT4 = PARSER_RESULT4.replace("COMPACTIONSTYLE","UNIV")
                        PARSER_RESULT5 = PARSER_RESULT5.replace("COMPACTIONSTYLE","UNIV")
                        RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE","UNIV")

                    RESULT_FILE = RESULT_FILE.replace("KEY",str(k))
                    RESULT_FILE = RESULT_FILE.replace("VALUE",str(v))
                    RESULT_FILE = RESULT_FILE.replace("BLOCKCACHE",str(c))
                    
                    #for p in PARSER_RESULTS : 
                        #p = p.replace("COMPACTIONSTYLE", "LVL" if i==0 else "UNIV" if i==1 else "FIFO")
                        #p = p.replace("KEY",str(k))
                        #p = p.replace("VALUE",str(v))
                        #p = p.replace("BLOCKCACHE",str(c))
                        #p = p.replace("BENCH", b)



                    PARSER_RESULT1 = PARSER_RESULT1.replace("KEY",str(k))
                    PARSER_RESULT1 = PARSER_RESULT1.replace("VALUE",str(v))
                    PARSER_RESULT1 = PARSER_RESULT1.replace("BLOCKCACHE",str(c))
                    PARSER_RESULT2 = PARSER_RESULT2.replace("KEY",str(k))
                    PARSER_RESULT2 = PARSER_RESULT2.replace("VALUE",str(v))
                    PARSER_RESULT2 = PARSER_RESULT2.replace("BLOCKCACHE",str(c))
                    PARSER_RESULT3 = PARSER_RESULT3.replace("KEY",str(k))
                    PARSER_RESULT3 = PARSER_RESULT3.replace("VALUE",str(v))
                    PARSER_RESULT3 = PARSER_RESULT3.replace("BLOCKCACHE",str(c))
                    PARSER_RESULT4 = PARSER_RESULT4.replace("KEY",str(k))
                    PARSER_RESULT4 = PARSER_RESULT4.replace("VALUE",str(v))
                    PARSER_RESULT4 = PARSER_RESULT4.replace("BLOCKCACHE",str(c))
                    PARSER_RESULT5 = PARSER_RESULT5.replace("KEY",str(k))
                    PARSER_RESULT5 = PARSER_RESULT5.replace("VALUE",str(v))
                    PARSER_RESULT5 = PARSER_RESULT5.replace("BLOCKCACHE",str(c))

                    RESULT_FILE = RESULT_FILE.replace("BENCH",b)
                    PARSER_RESULT1 = PARSER_RESULT1.replace("BENCH",b)
                    PARSER_RESULT2 = PARSER_RESULT2.replace("BENCH",b)
                    PARSER_RESULT3 = PARSER_RESULT3.replace("BENCH",b)
                    PARSER_RESULT4 = PARSER_RESULT4.replace("BENCH",b)
                    PARSER_RESULT5 = PARSER_RESULT5.replace("BENCH",b)

                    compaction_parser="python3 $PARSER/compaction_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                    latency_parser="python3 $PARSER/99parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                    avg_perf_parser="python3 $PARSER/{0}_averagePerformance_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT".format(b)
                    statistics_parser="python3 $PARSER/statistics_context_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                    perf_context_parser="python3 $PARSER/perf_context_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"


                    compaction_parser=compaction_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT1)
                    latency_parser=latency_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT2)
                    avg_perf_parser=avg_perf_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT3)
                    statistics_parser=statistics_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT4)
                    perf_context_parser=perf_context_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",PARSER_RESULT5)
                    
                    os.system(compaction_parser)
                    os.system(latency_parser)
                    os.system(avg_perf_parser)
                    os.system(statistics_parser)
                    os.system(perf_context_parser)

                    #print(compaction_parser)
                    #print(latency_parser)
                    #print(avg_perf_parser)

                    RESULT_FILE=OLDRESULT_FILE
                    PARSER_RESULT1=OLD1
                    PARSER_RESULT2=OLD2
                    PARSER_RESULT3=OLD3
                    PARSER_RESULT4=OLD4
                    PARSER_RESULT5=OLD5

print("*********** parser FIN ***************")

