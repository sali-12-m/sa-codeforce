t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    l=0
    r=n-1
    count=0
    while l<r and s[l]!=s[r]:
        count+=2
        l+=1
        r-=1
    print(n-count)
