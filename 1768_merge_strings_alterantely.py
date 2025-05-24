class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i= 0
        l1,l2=len(word1),len(word2)
        res=[]
        while i<max(l1,l2):
            if i<l1:
                res.append(word1[i])
            if i<l2:
                res.append(word2[i])
            i+=1
        
        return ''.join(res)
