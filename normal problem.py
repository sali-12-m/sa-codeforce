t=int(input())
for i in range(t):
    a=input()
    b=a[::-1]
    b=b.replace("p","a")
    b=b.replace("q","p")
    b=b.replace("a","q")
    print(b)
