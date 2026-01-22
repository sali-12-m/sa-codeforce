t= int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    found=False
    for i in range(n-1):
        if abs(a[i]-a[i+1])==5 or abs(a[i]-a[i+1])==7:
            found=True
        else:
            found=False
            break
    if found:
        print("YES")
    else:
        print("NO")
