class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        for i in range(numRows-1):
            b=[1]
            for j in range(i):
                b.append(res[i][j]+res[i][j+1])
            res.append(b+[1])
        return res