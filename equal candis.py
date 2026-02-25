t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mi=min(a)
    count=0
    for j in a:
        count+=j-mi
    print(count)
