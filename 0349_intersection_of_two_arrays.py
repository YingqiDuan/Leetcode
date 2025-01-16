class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in nums1:
            if i not in d:
                d[i] = 1
        
        l = []
        for i in nums2:
            if i in d and i not in l:
                l.append(i)

        return l
        