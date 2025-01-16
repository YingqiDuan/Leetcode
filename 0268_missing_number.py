class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        
        for i in range(n + 1):
            xor ^= i
           
        for num in nums:
            xor ^= num
            
        return xor

        # total = len(nums)*(len(nums)+1)//2
        # return total-sum(nums)