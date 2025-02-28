class Solution:
    def findLHS(self, nums: List[int]) -> int:
        s=dict()
        for n in nums:
            s[n]=s.get(n,0)+1

        c=0
        for i in s:
            if i+1 in s:
                c=max(c,s[i]+s[i+1])

        return c
