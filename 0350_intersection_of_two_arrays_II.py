class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1={}
        for i in nums1:
            if i not in n1:
                n1[i]=0
            n1[i]+=1
        
        n2={}
        for i in nums2:
            if i not in n2:
                n2[i]=0
            n2[i]+=1
        
        res=[]
        for i in n2:
            if i in n1:
                for _ in range(min(n1[i],n2[i])):
                    res.append(i) 
        return res
