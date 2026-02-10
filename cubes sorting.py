t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    found=True
    for j in range(1,n):
        if a[j]>=a[j-1]:
            found=False
            break
    if found:
        print("NO")
    else:
        print("YES")
      
