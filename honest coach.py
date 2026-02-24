t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ta=a[:n//2]
    tb=a[n//2:]
    li=[]
    for j in range(1,n):
        li.append(abs(a[j]-a[j-1]))
    print(min(li))
