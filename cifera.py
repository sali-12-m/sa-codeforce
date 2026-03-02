k=int(input())
l=int(input())
c=0
while l%k==0:
    l//=k
    c+=1
if l==1:
    print("YES")
    print(c-1)
else:
    print("NO")
