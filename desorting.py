t= int(input())
for j in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    if sorted(a)==a:
        m=a[1]-a[0]
        for i in range(1,n-1):
            m=min(m, a[i+1]-a[i])

        print(m//2 +1)
    else:
        print(0)
