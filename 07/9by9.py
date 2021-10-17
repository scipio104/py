#9by9.py
for x in range(1,10):
    print("%d の段"% x)
    for y in range(1,10):
        product=x*y
        print("%d,"% product,end="")
    print()
