t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mi=min(a)
    mx=max(a)
    print(mx-mi)
