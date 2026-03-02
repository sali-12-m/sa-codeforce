a,b,c,n=map(int,input().split())
va=a-c
vb=b-c
totv=va+vb+c
if c>a or c>b:
    print(-1)
elif n-totv >0:
    print(n-totv)
else:
    print(-1)
