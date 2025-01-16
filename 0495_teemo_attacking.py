class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        st = end = 0
        for t in timeSeries:
            if end > t:
                end = t + duration
            else:
                res += end - st
                st = t
                end = t + duration
        res += end - st
        return res