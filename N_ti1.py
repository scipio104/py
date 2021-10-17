#plot\scatter1import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

path='Boring.csv'
with open(path,encoding='utf-8') as f:
    f=csv.reader(f)
    all_csv=[row for row in f]
    csv_r=len(all_csv)
    csv_c=len(all_csv[0])

def pikup(list,position,new_list):
    for i in list[1:]:
        temp=float(i[position])
        new_list.append(temp)

d=[]
pikup(all_csv,0,d)
d=[i*-1 for i in d]

N=[]
pikup(all_csv,1,N)

print(N)
print(d)

fai=float(all_csv[1][4])
pile_head=float(all_csv[1][5])
pile_length=float(all_csv[1][6])
pile_tip=pile_head+pile_length

print(fai,pile_head,pile_length,pile_tip)

NU=(-4*fai/1000+pile_tip)*-1
NB=(fai/1000+pile_tip)*-1

NUB=list([NU,NB])
print(NUB)

for i in NUB:
    if i not in d:
        d.append(i)
        d.sort(reverse=True)
NUi=d.index(NU)
NBi=d.index(NB)

N.insert(NUi,0)
N.insert(NBi,0)

print(d)
print(N)
print(NUi,NBi)

#未確定N値位置
d_fast=abs(d[NUi+1]-d[NUi])
d_last=abs(d[NBi]-d[NBi-1])
print(d_fast,d_last)
#未確定N値
if d_fast<1:
    N1=(N[NUi+1]-N[NUi-1])*(d[NUi]-d[NUi-1])-N[NUi-1]
    N[NUi]=abs(round(N1,2))
if d_last<1:
    N2=(N[NBi+1]-N[NBi-1])*(d[NBi]-d[NBi-1])-N[NBi-1]
    N[NBi]=abs(round(N2,2))
print(N)

sh=0
sa=0
for i in range(NUi,NBi):
    u=N[i]
    b=N[i+1]
    print(u,b)
    h=abs(d[i+1]-d[i])
    print(h)
    a=(u+b)*h/2
    sh=sh+h
    sa=sa+a
HN=sa/sh
print(round(HN,2))

ph=np.array([20,20,20+fai/400,20+fai/400])
pd=np.array([pile_head*-1,pile_tip*-1,pile_tip*-1,pile_head*-1])

plt.plot([0,20+fai/400],[NU,NU])
plt.plot([0,20+fai/400],[NB,NB])
plt.plot(N,d)
plt.plot(ph,pd)
plt.show()
