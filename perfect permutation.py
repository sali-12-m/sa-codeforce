n=int(input())
if n%2==1:
    print(-1)
else :
    li=[]
    for I in range (1,n+1,2):
        li.append(I+1)
        li.append(I)
    print(*li)