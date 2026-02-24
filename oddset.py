t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ce=0
    co=0
    for j in a:
        if j%2==0:
            ce+=1
        else:
            co+=1
    if ce==co:
        print("YES")
    else:
        print("NO")
