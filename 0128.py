class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set=set(nums)
        longest=0

        for n in num_set:
            if n-1 not in num_set:
                length=1
                curr=n
                while curr+1 in num_set:
                    curr+=1
                    length+=1
                
                longest=max(longest,length)
        
        return longest