
left_margin=2.8
bottom_margin=3.8
dx=3.6
dy=3.2
nx=9
ny=9
xs=(nx-1)
ys=(ny-1)
for i in range(0,nx):
    x=left_margin+i*dx
    for j in range(0,ny):
        y=bottom_margin+j*dy
        print("%.1f,%.1f"%(x,y))
print()
