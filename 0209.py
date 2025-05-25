class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        l=0
        cur_sum=0
        m_len=float('inf')
        
        for r in range(n):
            cur_sum+=nums[r]

            while cur_sum>=target:
                m_len=min(m_len,r-l+1)
                cur_sum-=nums[l]
                l+=1
        
        return 0 if m_len==float('inf') else m_len
