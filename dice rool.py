y,w=map(int,input().split())
m=max(y,w)-1
d=6-m
if d==0:
    print("0/6")
elif d==1:
    print("1/6")
elif d==2:
    print("1/3")
elif d==3:
    print("1/2")
elif d==4:
    print("2/3")
elif d==5:
    print("5/6")
else:
    print("1/1")
