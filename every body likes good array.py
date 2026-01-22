t= int(input())
for j in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=1
    opp=0
    for i in range(1,n):
        if a[i]%2==a[i-1]%2:
            count+=1
        else:
            opp+=count-1
            count=1
    opp+=count-1
    print(opp)
