n = int(input())
fib = [0, 1]
while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
if n == 0:
    print(0, 0, 0)
elif n == 1:
    print(0, 0, 1)
elif n == 2:
    print(0, 1, 1)
else:
    k = fib.index(n)
    print(fib[k-1], fib[k-3], fib[k-4])
