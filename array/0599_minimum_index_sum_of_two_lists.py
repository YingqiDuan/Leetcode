class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l={s:i for i,s in enumerate(list1)}
        _min=float('inf')
        res=[]

        for i,s in enumerate(list2):
            if s in l:
                _sum=l[s]+i
                if _sum<_min:
                    _min=_sum
                    res=[s]
                elif _sum==_min:
                    res.append(s)
        
        return res

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    l.append([i+j,list1[i]])
                    break
        l.sort()
        res=[s for i,s in l if i==l[0][0]]
        return res