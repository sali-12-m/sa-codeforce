s=input()
cu=0
cl=0
for i in s:
    if i.isupper():
        cu+=1
    else:
        cl+=1
if cu==cl:
    print(s.lower())
elif cu>cl:
    print(s.upper())
else:
    print(s.lower())
