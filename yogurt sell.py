t=int(input())
for i in range(t):
    n, a, b = map(int, input().split())
    if 2 * a > b:
        if n % 2 == 0:
            print(n // 2 * b)
        else:
            print(n // 2 * b + a)
    else:
        print(n * a)
