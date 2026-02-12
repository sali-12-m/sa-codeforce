al=list("abcdefghijklmnopqrstuvwxyz")
s=input()
current="a"
count=0
for i in s:
    pc=al.index(current)
    pt=al.index(i)
    cl=abs(pt-pc)
    cw=26-cl
    count+=min(cl,cw)
    current=i
print(count)
