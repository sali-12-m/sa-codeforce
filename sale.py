n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
count=0
for i in range(m):
    if a[i]<0:
        count+=a[i]
print(abs(count))
