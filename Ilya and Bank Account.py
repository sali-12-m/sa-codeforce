n=int(input())
if n>=0:
    print(n)
else:
    s=str(n)
    s1=int(s[:-1])
    s2=int(s[:-2]+s[-1])
    print(max(s1,s2))
