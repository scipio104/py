#nested_for.py
xy=((1,2),(3,4),(5,6),(7,8),(9,10),(11,12))
total=0
for x,y in xy:
  print("X=%d,y=%d"% (x,y))
  total+=x*y
print("total=",total)
