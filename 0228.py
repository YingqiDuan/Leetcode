class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges=[]
        n=len(nums)
        if n==0:
            return ranges
        
        start=nums[0]
        prev=nums[0]

        for i in range(1,n):
            curr=nums[i]
            if curr!=prev+1:
                if start==prev:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{prev}")
                start=curr
            prev=curr
        
        if start==prev:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{prev}")
        
        return ranges
