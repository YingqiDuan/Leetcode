class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0  # current jump range
        farthest = 0  # next jump

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # reach jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= len(nums) - 1:
                    break

        return jumps
