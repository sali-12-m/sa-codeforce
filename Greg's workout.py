n = int(input())
a = list(map(int, input().split()))
ba = 0
bi = 0
ch = 0
for i in range(n):
    if i % 3 == 0:
        ch += a[i]
    elif i % 3 == 1:
        bi += a[i]
    else:
        ba += a[i]
if ba > bi and ba > ch:
    print("back")
elif bi > ba and bi > ch:
    print("biceps")
else:
    print("chest")