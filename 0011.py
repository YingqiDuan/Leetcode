class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        v=0

        while l<r:
            h=min(height[l],height[r])
            w=r-l
            v=max(v,h*w)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return v