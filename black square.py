a1,a2,a3,a4=map(int,input().split())
s=input()
count=0
for i in s:
    if i=="1":
        count+=a1
    elif i=="2":
        count+=a2
    elif i=="3":
        count+=a3
    else:
        count+=a4
print(count)
