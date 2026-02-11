n,h=map(int,input().split())
a=list(map(int,input().split()))
cu=0
cn=0
for i in range(n):
    if a[i]<=h:
        cu+=1
    else:
        cn+=2
print(cu+cn)
