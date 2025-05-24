def canJump(nums):
    maxReach = 0
    l = len(nums)

    for i in range(l):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + nums[i])
        if maxReach >= l - 1:
            return True
    return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        while i > 0:
            j = i - 1
            while j >= 0:
                if i - j <= nums[j]:
                    i = j
                    break
                else:
                    j -= 1
            if j < 0:
                return False
        return True
