t=int(input())
for j in range(t):
    a,b,c=map(int, input().split())
    if a>b:
        print("First")
    elif a<b:
        print("Second")
    else:
        if c%2!=0:
            print("First")
        else :
            print("Second")   