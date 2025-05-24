class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w=sum(nums[:k])
        m=w

        for i in range(k,len(nums)):
            w+=nums[i]-nums[i-k]
            if w>m:
                m=w
        return m/k