t = int(input())
for j in range(t):
    n, m = map(int, input().split())
    s = input()
    count = 0
    for i in "ABCDEFG":
        a= s.count(i)
        if a < m:
            count += m-a
    print(count)