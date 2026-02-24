k,n,w=map(int,input().split())
count=0
for i in range(1,w+1):
    count+=i*k
if n>=count:
    print(0)
else:
    print(count-n)
