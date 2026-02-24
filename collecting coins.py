t=int(input())
for i in range(t):
    a,b,c,n=map(int,input().split())
    m=max(a,b,c)
    ma=m-a
    mb=m-b
    mc=m-c
    mt=ma+mb+mc
    if n-mt<0:
        print("NO")
    elif (n-mt)%3==0:
        print("YES")
    else:
        print("NO")
