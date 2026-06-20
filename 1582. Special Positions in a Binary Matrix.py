class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0
        for i in range(len(mat)):
            s= mat[i].count(1)
            for j in range(len(mat[0])):
                c=sum(mat[k][j] for k in range(len(mat)))
                if mat[i][j]==1 and s==1==c:
                    count+=1
        return count
