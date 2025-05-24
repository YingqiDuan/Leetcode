class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        nums=[lower-1]+nums+[upper+1]
        prev = nums[0]
        
        for i in range(1,len(nums)):
            cur = nums[i]
            if prev + 1 <= cur - 1:
                res.append([prev + 1, cur - 1])
            prev = cur
        return res