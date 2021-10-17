#countrand01.py
import random as rnd
rnd.seed(2)
count=0
luckynum=777
max=1000
randnum=-1
while randnum !=luckynum:
  randnum=rnd.randrange(max)
  count+=1
print("%d回目に%dが出ました!"%(count,randnum))
'''123
456
789'''
