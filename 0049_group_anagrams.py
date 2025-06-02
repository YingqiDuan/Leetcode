class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        for s in strs:
            i=''.join(sorted(s))
            if i not in d:
                d[i]=[]
            d[i].append(s)
        
        res=[]
        for j in d.values():
            res.append(j)
        return res

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)        
        for word in strs:
            key = ''.join(sorted(word))   
            groups[key].append(word)
        return list(groups.values())
