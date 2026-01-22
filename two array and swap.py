t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for I in range(k):
        m1=min(a)
        m2=max(b)
        if m1<m2:
            x=a.index(m1)
            y=b.index(m2)
            a[x],b[y]=b[y],a[x]
        else:
            break
    print(sum(a))
