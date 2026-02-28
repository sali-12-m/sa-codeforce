t=int(input())
for i in range(t):
    n,f,a,b=map(int,input().split())
    m=list(map(int,input().split()))
    p=0
    found=True
    ti=f
    for j in m:
        g=j-p
        c=min(g*a,b)
        ti-=c
        if ti<=0:
            found=False
            break
        p=j
    if found:
        print("YES")
    else:
        print("NO")
