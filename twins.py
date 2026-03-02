n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
tot=sum(a)//2
ms=0
i=0
while tot>=ms:
    ms+=a[i]
    i+=1
print(i)
