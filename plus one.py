class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        s = ""
        for i in range(len(d)):
            s += str(d[i])
        num = int(s) + 1
        n=str(num)
        li=[]
        for i in n:
            li.append(int(i))
        return li
