#forcalc01.py
pairs=[[3.5,9.0],[2.3,5.3],[4.4,5.6]]
sumxy=0
sumx=0
sumy=0
z=len(pairs)
for x,y in pairs:
  print("%.1f %.1f"%(x,y))
  sumxy+=x*y
  sumx+=x/z
  sumy+=y/z
print(sumxy)
print("%.2f"%sumx)
print("%.2f"%sumy)
