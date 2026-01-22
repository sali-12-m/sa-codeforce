t= int(input())
for j in range(t):
    s1=input()
    s2=input()
    sum=0
    for i in range (1,len(s2)):
        postpos=s1.index(s2[i])
        prevpos=s1.index(s2[i-1])
        sum+=abs(postpos-prevpos)
    print(sum)
