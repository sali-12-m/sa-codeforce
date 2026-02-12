n=int(input())
a=list(map(int,input().split()))
ps=0
c=0
for i in a:
    if i==-1:
        if ps==0:
            c+=1
        else:
            ps-=1
    else:
        ps+=i
print(c)
