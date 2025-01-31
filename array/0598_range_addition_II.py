class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for x,y in ops:
            if m>x:
                m=x
            if n>y:
                n=y
        return m*n