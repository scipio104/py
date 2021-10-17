import pandas as pd
import numpy as ny
#wave=[]
path='kekka2.csv'
with open(path) as f:
    f=f.readlines()
id=[]
idn=[]
n=0
m=0

for s in f:
    n+=1
    if 'name' in s:
        id.append(s)
        idn.append(n)
        m+=1
print(m)
for i in range(m):
    print(idn[i])
    print(id[i])
l_XXX_i = [i for i, line in enumerate(f) if 'name' in line]
print(l_XXX_i)
# [0, 3, 4]
