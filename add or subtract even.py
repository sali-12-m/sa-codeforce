t=int(input())
for j in range(t):
    a,b=map(int,input().split())
    if a==b:
        print(0)
    elif a<b:
        c=b-a
        if c%2==1:
            print(1)
        else:
            print(2)
    else:
        c=a-b
        if c%2==0:
            print(1)
        else:
            print(2)