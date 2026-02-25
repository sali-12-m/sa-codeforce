t=int(input())
for i in range(t):
    n=int(input())
    k=2
    while True:
        if n%(2**k -1)==0:
            break
        k+=1
    print(n//(2**k -1))
