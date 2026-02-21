n=int(input())
a=list(map(int,input().split()))
mi=min(a)
ma=max(a)
count=0
for i in a:
    if mi<i<ma:
        count+=1
print(count)
