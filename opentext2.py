import pandas as pd
import numpy as np
import csv

path='kekka2.csv'
with open(path) as f:
    f=csv.reader(f)
    l=[row for row in f]
    #for row in f[0,10]:

    #f=csv.reader(f)
    #l=[row for row in f]
    xspn=[i for i in l if 'Xスパン数' in i]
#xs1=xspn.split(',')
#xs=xs1[0]
#print(xspn)
#print(xs)

    id= [(i,line) for i, line in enumerate(l) if 'name' in line]
#idn= [i for i in enumerate(f) if 'name' in line]
#e=len(f)
    #e1=len(id)
#for i in id:
    tar="name=支持力検討用軸力表（グリッド形式）"
    idN= [(i,line) for i, line in enumerate(f) if tar in line]
    idn1=idN[0]
    print(idN)
    print("---")
    idn1=idn1[0]
    print(type(idn1))
    print(idn1)
    n=0

    for i in range(idn1,idn1+5):
        if len(f[i])==0:
            break
            a=f[i]
            print(a)
        n+=1
#print(a)
