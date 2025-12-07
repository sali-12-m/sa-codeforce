t= int(input())
for I in range(t):
    a=int(input())
    n= 360%(180-a)
    if n==0:
        print("YES")
    else:
        print("NO")    