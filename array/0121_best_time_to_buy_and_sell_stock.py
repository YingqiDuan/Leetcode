class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=prices[0]
        res=0
        for p in prices:
            res=max(res,p-b)
            if p<b:
                b=p
        return res