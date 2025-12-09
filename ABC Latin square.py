t = int(input())
for _ in range(t):
    s1 = input().strip()
    s2 = input().strip()
    s3 = input().strip()
    for i in (s1,s2,s3):
        if "?" in i:
            for j in "ABC":
                if j not in i:
                    print(j)