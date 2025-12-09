t= int(input())
for I in range(t):
    n=int(input())
    l={}
    for j in range(1,n+1):
        a,b=map(int,input().split())
        if a<=10:
           l[j]=b 
    m=max(l,key=l.get)     
    print(m)        
        