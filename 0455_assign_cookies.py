class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j,res=0,0,0
        li,lj=len(g),len(s)
        while i<li and j<lj:
            if s[j]>=g[i]:
                i+=1
                res+=1
            j+=1
        return res