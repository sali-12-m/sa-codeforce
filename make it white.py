t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    li=[]
    for j in range(n):
        if s[j]=="B":
            li.append(j)
    print(max(li)-min(li)+1)
