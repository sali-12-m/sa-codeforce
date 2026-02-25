t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    ma=max(a)
    li=[]
    for j in range(3):
        if a[j]==ma and a.count(ma)==1:
            li.append(0)
        else:
            li.append(ma-a[j]+1)
    print(*li)
