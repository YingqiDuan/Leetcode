class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[1]
        for i in range(rowIndex):
            b=[1]
            for j in range(i):
                b.append(res[j]+res[j+1])
            res=b+[1]
        return res