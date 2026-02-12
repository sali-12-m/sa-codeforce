n=int(input())
t=list(map(int,input().split()))
l=0
r=n-1
s=0
d=0
for i in range(n):
    if t[l]>t[r]:
        v=t[l]
        l+=1
    else:
        v=t[r]
        r-=1
    if i%2==0:
        s+=v
    else:
        d+=v
print(s,d)
