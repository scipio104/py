#countrand01.py
import random as rnd
rnd.seed(2)
count=0
luckynum=777
max=1000
#randum=-1
while True:
    count+=1
    if rnd.randrange(max)==luckynum:
        break
print("%d回目に%dが出ました!"%(count,luckynum))
