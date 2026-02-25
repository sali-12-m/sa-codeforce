t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    li=[]
    for j in range(n):
        if a[j]==b[-1]:
            a[j]=(a[j]-b[-2])
        else:
            a[j]=(a[j]-b[-1])
    print(*a)
