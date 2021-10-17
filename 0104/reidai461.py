#reidai461
import sys
year=int(sys.argv[1])
A=(year%4==0)
B=(year%100==0)
C=(year%1000==0)
if (A and (not B))or C:
  print("%d年はうるう年です。"% year)
else:
  print("%d年は平年です。"% year)
