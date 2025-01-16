class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        for i in nums:
            if i > nums[j-1]:
                nums[j]=i
                j+=1
        return j