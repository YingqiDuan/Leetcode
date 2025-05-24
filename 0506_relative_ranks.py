class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=sorted(score, reverse=True)
        d=dict()
        for i,n in enumerate(s):
            if i>2:
                d[n]=str(i+1)
            elif i==0:
                d[n]="Gold Medal"
            elif i==1:
                d[n]="Silver Medal"
            else:
                d[n]="Bronze Medal"
        return [d[s] for s in score]
            
