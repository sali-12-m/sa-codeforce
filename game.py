n=int(input())
ho=[]
aw=[]
for i in range (n):
    h,a=map(int,input().split())
    ho.append(h)
    aw.append(a)
count=0
for j in range(n):
    for k in range(n):
        if j!=k:
            if ho[j]==aw[k]:
                count+=1
print(count)
