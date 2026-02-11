for i in range(5):
    a =list(map(int, input().split()))
    if 1 in a:
        r = i
        c = a.index(1)
print(abs(r-2)+abs(c-2))
