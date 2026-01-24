t= int(input())
for j in range(t):
    n=int(input())
    s=input()
    if "U" in s:
        a=s.replace("U","D")
        print(a)
    elif "D" in s:
        a=s.replace("D","U")
        print(a)
    else:
        print(s)