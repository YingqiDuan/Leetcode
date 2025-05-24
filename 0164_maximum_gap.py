class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        c = nums[0]
        for i in nums:
            if i - c > res:
                res = i - c
            c = i
        return res
