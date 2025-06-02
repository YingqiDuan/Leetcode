class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx={}

        for i,v in enumerate(nums):
            if v in idx:
                prev=idx[v]
                if i-prev<=k:
                    return True
            idx[v]=i
            
        return False
            

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()

        for i,v in enumerate(nums):
            if v in window:
                return True
            
            window.add(v)

            if i>=k:
                window.remove(nums[i-k])

        return False            
