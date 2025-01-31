class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        t=0
        for i in nums:
            if i==0:
                res=max(res,t)
                t=0
            else:
                t+=1
        return max(res,t)