class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start,end=0,len(nums)
        while start<end:
            mid=(start+end)>>1
            if nums[mid]<target:
                start=mid+1
            else:
                end=mid
        return start