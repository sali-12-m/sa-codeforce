n = int(input())
s=[]
for k in range(n):
    s.append(input())
count = 0
for i in range(len(s[0])):
    for j in range(1, n):
        if s[j][i] != s[0][i]:
            print(count)
            exit()
    count += 1
print(count)
