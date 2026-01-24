t= int(input())
for j in range(t):
    x=int(input())
    a=list(map(int,input().split()))
    found=True
    for i in range(3):
        if x==0:
            found=False
            break
        x=a[x-1]
    if found:
        print("YES")
    else:
        print("NO")