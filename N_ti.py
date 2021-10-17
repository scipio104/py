#plot\scatter1import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

N=[]
d=[]
n=0

fai=500
pile_b=14
ph=np.array([20,20,20+fai/400,20+fai/400])
pd=np.array([-1,pile_b*-1,pile_b*-1,-1])


NU=(-4*fai/1000+pile_b)*-1
NB=(fai/1000+pile_b)*-1
N0=pile_b*-1
NUB=list([NU,NB])
print(NUB)
plt.plot([0,20+fai/400],[NU,NU])
plt.plot([0,20+fai/400],[NB,NB])



pi=3.141593
p2=2*pi
dt=0.5
fk=[]

f= np.loadtxt('N_rei.csv') #,skiprows=5)
for i in f:
    N.append(i)
    n-=1
    d.append(n)
for Nh in NUB:
    if Nh not in d:
        d.extend([Nh])
        d.sort(reverse=True)
        kn=d.index(Nh)
        N.insert(kn,0)
print(d)

nou=d.index(NU)
nob=d.index(NB)
print(nou)
print([nou+1],[nou-1])
print(N[nou+1],N[nou-1])
print(d[nou+1],d[nou-1])

d1=abs(d[nou+1]-d[nou])
d2=abs(d[nob]-d[nob-1])
print(d1,d2)
if d1>=1:
    N1=N[nou]
else:
    N1=(N[nou+1]-N[nou-1])*(d[nou]-d[nou-1])-N[nou-1]
    N[nou]=abs(round(N1,2))
if d2>=1:
    N2=N[nob]
else:
    N2=(N[nob+1]-N[nob-1])*(d[nob]-d[nob-1])-N[nob-1]
    N[nob]=abs(round(N2,2))
print(N1,N2)
print("---")
print(N)
sh=0
sa=0
for i in range(nou+1,nob+1):
    u=N[i-1]
    b=N[i]
    print(u,b)
    h=abs(d[i]-d[i-1])
    a=(u+b)*h/2
    sh=sh+h
    sa=sa+a
HN=sa/sh
round(HN,2)
print(round(sh,2),round(sa,2))

print(round(HN,2))
plt.plot(N,d)
plt.plot(ph,pd)
plt.show()
