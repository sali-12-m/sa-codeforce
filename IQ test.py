n=int(input())
a=list(map(int,input().split()))
ce=0
co=0
for i in range(n):
    if a[i]%2==0:
        ce+=1
    else:
        co+=1
if ce==1:
    for j in range(n):
        if a[j]%2==0:
            print(j+1)
            break
else:
    for j in range(n):
        if a[j]%2!=0:
            print(j+1)
            break
