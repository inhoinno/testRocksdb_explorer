import os
import re
import sys
from collections import defaultdict
DEV_PATH="../mnt"
RESULT_PATH="../result_txt"

if len(sys.argv) == 1 : 
    testname = "uniformtest_fig4"
else :
    testname = sys.argv[1]


#UM= 55000000 #~25GB
#UM=110000000  #~50GB
#UM=210000000  #100.13GB
#UM=1250000000 #596.04GB

# INPUT FILES
RESULT_FILE="{0}_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE_lLEVEL0_mMINMERGE_countCOUNT_rdonlyRDONLY.txt".format(testname)
OLDRESULT_FILE = RESULT_FILE
LOG_FILE = "LOG_{0}_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE_lLEVEL0_mMINMERGE_countCOUNT_rdonlyRDONLY".format(testname)
OLDLOG_FILE=LOG_FILE
NAME="{0}_report_readamp_COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE_lLEVEL0_mMINMERGE_countCOUNT_rdonlyRDONLY.csv".format(testname)
OLDNAME=NAME

key_vars=[16]#,32,64,128,256,1024]
value_vars=[64]#,128,256,512,1024,4096]
cache_vars=[512] 
l0_vars=[4] # default : 4
min_merge_width_vars = [2] # default : 2
rdonly_vars=[1,0] #true, false
#target_num = (256+256)*NUM

#d = defaultdict(dict)
#for k in key_vars:
    #for v in value_vars:
        #d[k][v] = int(target_num/(k+v))
        #print(k,v,target_num/(k+v))
#print(d[256][256])

compactionstyle=[0,1]
benchmark=["fillrandom","readrandom", "fillseq","readseq"]

#benchmark=["fillseq", "readseq"]
I=0
bench=""

## OUTPUT FILES
tailname = "COMPACTIONSTYLE_BENCH_kKEY_vVALUE_cBLOCKCACHE_lLEVEL0_mMINMERGE_countCOUNT_rdonlyRDONLY.csv"

PARSER="../python_parser"
PARSER_RESULT1="{0}_compaction_count_{1}".format(testname,tailname)
PARSER_RESULT2="{0}_99_{1}".format(testname,tailname)
PARSER_RESULT3="{0}_avg_{1}".format(testname,tailname)
PARSER_RESULT4="{0}_statistics_{1}".format(testname,tailname)
PARSER_RESULT5="{0}_perf_context_{1}".format(testname,tailname)
PARSER_RESULT6="{0}_WA_{1}".format(testname,tailname)
PARSER_RESULT7="{0}_per_compaction_size_{1}".format(testname,tailname)

OLD1=PARSER_RESULT1
OLD2=PARSER_RESULT2
OLD3=PARSER_RESULT3
OLD4=PARSER_RESULT4
OLD5=PARSER_RESULT5
OLD6=PARSER_RESULT6
OLD7=PARSER_RESULT7

RESULT_FILE=OLDRESULT_FILE

PARSER_RESULTS = [PARSER_RESULT1, PARSER_RESULT2, PARSER_RESULT3, PARSER_RESULT4, PARSER_RESULT5, PARSER_RESULT6, PARSER_RESULT7]

for count in range(0,1):
    for i in compactionstyle:
        for k in key_vars:
            for v in value_vars:
                for c in cache_vars:
                    for b in benchmark:
                        for l in l0_vars:
                            for minmerge in min_merge_width_vars:
                                for rdonly in rdonly_vars:
                                    m=minmerge

                                    BENCHMARK="{0},levelstats,stats".format(b)

                                    RESULT_FILE = RESULT_FILE.replace("COMPACTIONSTYLE", "LVL" if i==0 else "UNIV" if i==1 else "FIFO")
                                    RESULT_FILE = RESULT_FILE.replace("KEY",str(k))
                                    RESULT_FILE = RESULT_FILE.replace("VALUE",str(v))
                                    RESULT_FILE = RESULT_FILE.replace("BLOCKCACHE",str(c))
                                    RESULT_FILE = RESULT_FILE.replace("LEVEL0",str(l))
                                    RESULT_FILE = RESULT_FILE.replace("MINMERGE",str(minmerge))
                                    RESULT_FILE = RESULT_FILE.replace("BENCH",b) 
                                    RESULT_FILE = RESULT_FILE.replace("COUNT", str(count))
                                    RESULT_FILE = RESULT_FILE.replace("RDONLY", str(rdonly))
                                    LOG_FILE = LOG_FILE.replace("COMPACTIONSTYLE", "LVL" if i==0 else "UNIV" if i==1 else "FIFO")
                                    LOG_FILE = LOG_FILE.replace("KEY",str(k)).replace("VALUE",str(v)).replace("BLOCKCACHE",str(c)).replace("BENCH",b).replace("LEVEL0",str(l)).replace("MINMERGE",str(minmerge)).replace("COUNT",str(count)).replace("RDONLY", str(rdonly))
                                    for p in PARSER_RESULTS : 
                                        p = p.replace("COMPACTIONSTYLE", "LVL" if i==0 else "UNIV" if i==1 else "FIFO")
                                        p = p.replace("KEY",str(k))
                                        p = p.replace("VALUE",str(v))
                                        p = p.replace("BLOCKCACHE",str(c))
                                        p = p.replace("LEVEL0",str(l))
                                        p = p.replace("MINMERGE",str(minmerge))
                                        p = p.replace("BENCH", b)
                                        p = p.replace("COUNT",str(count))
                                        p = p.replace("RDONLY", str(rdonly))

                                        if re.search('99',p)!=None:
                                            latency_parser ="python3 $PARSER/99parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                                            latency_parser=latency_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",p)
                                            os.system(latency_parser)

                                        elif re.search('avg',p)!=None:
                                            avg_perf_parser="python3 $PARSER/{0}_averagePerformance_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT".format(b)
                                            avg_perf_parser=avg_perf_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",p)
                                            os.system(avg_perf_parser)

                                        elif re.search('statistics',p)!=None:
                                            statistics_parser="python3 $PARSER/statistics_context_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                                            statistics_parser=statistics_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",p)
                                            os.system(statistics_parser)

                                        elif re.search('perf',p)!=None:
                                            perf_context_parser="python3 $PARSER/perf_context_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                                            perf_context_parser=perf_context_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",p)
                                            os.system(perf_context_parser)

                                        elif re.search('WA',p)!=None:
                                            WA_parser="python3 $PARSER/WA_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                                            WA_parser=WA_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",p)
                                            os.system(WA_parser)

                                        elif re.search('compaction_count',p)!=None  :
                                            compaction_parser="python3 $PARSER/compaction_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                                            compaction_parser=compaction_parser.replace("$PARSER", PARSER,2).replace("$RESULT_PATH",RESULT_PATH,2).replace("$RESULT_FILE",RESULT_FILE,2).replace("$PARSER_RESULT",p)
                                            os.system(compaction_parser)

                                        elif re.search('per_compaction_size',p)!=None :
                                            per_compaction_size_parser = "python3 $PARSER/LOG_parser.py $RESULT_PATH/$RESULT_FILE $PARSER/csv/$PARSER_RESULT"
                                            per_compaction_size_parser = per_compaction_size_parser.replace("$PARSER",PARSER,2).replace("$RESULT_PATH","../logs").replace("$RESULT_FILE",LOG_FILE,2).replace("$PARSER_RESULT",p)
                                            os.system(per_compaction_size_parser)

                                             


                                    #print(compaction_parser)
                                    #print(latency_parser)
                                    #print(avg_perf_parser)

                                    RESULT_FILE=OLDRESULT_FILE
                                    LOG_FILE = OLDLOG_FILE

print("*********** parser FIN ***************")

