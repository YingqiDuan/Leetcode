class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d=-1
        m=-1

        for n in nums:
            i=abs(n)-1
            if nums[i]<0:
                d=abs(n)
            else:
                nums[i]=-nums[i]
        
        for i in range(len(nums)):
            if nums[i]>0:
                m=i+1
                break
        
        return [d,m]
