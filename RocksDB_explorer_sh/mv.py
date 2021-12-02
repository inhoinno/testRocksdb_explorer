import os 
t=16
k=16
b="fillrandom"
os.system("mv ../mnt/LOG ../logs/LOG_test{0}_COMPACTION_k{1}_v{2}".replace("COMPACTION","LVL").format(t,k,b))
#print("mv ../mnt/LOG ../logs/LOG_test{0}_COMPACTION_k{1}_b{2}".replace("COMPACTION","LVL").format(t,k,b))
