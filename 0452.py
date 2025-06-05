class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda interval:interval[1])

        arrows=1
        current_arrow_pos=points[0][1]

        for x_start,x_end in points[1:]:
            if x_start>current_arrow_pos:
                arrows+=1
                current_arrow_pos=x_end
        
        return arrows