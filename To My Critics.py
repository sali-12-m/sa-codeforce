t= int(input())
for I in range(t):
    a,b,c=map(int,input().split())
    x=a+b
    y=a+c
    z=b+c
    if x>=10 or y>=10 or z>=10:
        print("YES")
    else:
        print("NO")
