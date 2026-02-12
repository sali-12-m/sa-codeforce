n=int(input())
s=input()
li=list(s)
count=0
for i in range(1,n):
    if li[i]==li[i-1]:
        count+=1
print(count)
