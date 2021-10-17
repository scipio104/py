# csvlib_read.py
import sys
import csv
csvfile=sys.argv[1]
with open(csvfile)as cf:
  data=csv.reader(cf)
  for row in data:
    print("\t".join(row))
