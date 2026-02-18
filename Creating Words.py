t=int(input())
for i in range(t):
    a,b=input().split()
    a1=list(a)
    b1=list(b)
    a1[0],b1[0]=b1[0],a1[0]
    print("".join(a1),"".join(b1))
