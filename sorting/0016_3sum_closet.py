class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            #early stop
            c_min = nums[i] + nums[i + 1] + nums[i + 2]
            if c_min >= target:
                if abs(c_min - target) < abs(best - target):
                    best = c_min
                break
            
            c_max = nums[i] + nums[n - 2] + nums[n - 1]
            if c_max <= target:
                if abs(c_max - target) < abs(best - target):
                    best = c_max
                continue
            
            #two points
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(current_sum - target) < abs(best - target):
                    best = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        return best

