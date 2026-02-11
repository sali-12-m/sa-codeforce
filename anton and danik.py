n=int(input())
s=input()
ca=0
cd=0
li=list(s)
for i in li:
    if i=="A":
        ca+=1
    else:
        cd+=1
if cd>ca:
    print("Danik")
elif cd<ca:
    print("Anton")
else:
    print("Friendship")
