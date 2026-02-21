t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    d=abs(a-b)
    n=2*d
    if d==0 or max(a,b,c)>n:
        print(-1)
        continue
    if c+d<=n:
        print(c+d)
    else:
        print(c-d)
