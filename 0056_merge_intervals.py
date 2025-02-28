class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # Sort intervals based on the starting time
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in intervals[1:]:
            last = res[-1]
            # If the current interval overlaps with the last interval in merged
            if i[0] <= last[1]:
                # Merge the intervals by updating the end of the last interval
                last[1] = max(last[1], i[1])
            else:
                res.append(i)
        return res
