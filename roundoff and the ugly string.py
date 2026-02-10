t = int(input())
for j in range(t):
    n = int(input())
    s = input()
    i = 0
    d= 0
    while i <= n - 3:
        if s[i:i+3] == "map" or s[i:i+3] == "pie":
            d+= 1
            i+= 3
        else:
            i+= 1
    print(d)
