class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        a=b=-1
        c=len(wordsDict)
        for i,w in enumerate(wordsDict):
            if w==word1:
                a=i
            if w==word2:
                b=i
            if a!=-1 and b!=-1:
                c=min(c,abs(a-b))
        return c