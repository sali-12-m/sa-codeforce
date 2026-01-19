t= int(input())
for j in range(t):
    x,y=map(int,input().split())
    if x>y:
        print(y,x)
    elif y>x:
        print(x,y)
    else:
        print(x,y)