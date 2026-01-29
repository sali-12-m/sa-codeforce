s=input()
w="heidi"
i=0
for j in s:
    if j==w[i]:
        i+=1
        if i==len(w):
            break
if i==len(w):
    print("YES")
else:
    print("NO")
