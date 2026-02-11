n=int(input())
count=0
for i in range(n):
    p=list(map(int,input().split()))
    c1=p.count(1)
    c0=p.count(0)
    if c1>c0:
        count+=1
print(count)
