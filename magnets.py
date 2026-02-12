n=int(input())
count=0
li=[]
for i in range(n):
    m=int(input())
    li.append(m)
for j in range(1,n):
    if li[j]!=li[j-1]:
        count+=1
print(count+1)
