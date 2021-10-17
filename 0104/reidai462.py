#reidai462
import sys
year=int(sys.argv[1])
if (year%4==0 and year%100!=0)or year%1000==0:
  print("%d年はうるう年です。"% year)
else:
  print("%d年は平年です。"% year)
