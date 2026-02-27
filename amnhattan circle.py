t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    li=[]
    g=[]
    for j in range(n):
        g.append(input().strip())
    for j in range(n):
        for k in range(m):
            if g[j][k] == "#":
                li.append((j+1,k+1))
    mid = len(li) // 2
    print(li[mid][0], li[mid][1])
