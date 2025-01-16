class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res=[]
        p=nums[0]
        nums.append(nums[-1]+2)
        
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]>1:
                res.append(f"{p}->{nums[i]}") if nums[i]!=p else res.append(f"{p}")
                p=nums[i+1]
        return res
