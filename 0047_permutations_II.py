class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used):
            # If the path reaches the length of nums, it is a valid permutation
            if len(path) == len(nums):
                res.append(path[:])
            for i in range(len(nums)):
                # Skip used elements
                if used[i]:
                    continue
                # Skip duplicate
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path, used)

                # backtrack
                path.pop()
                used[i] = False

        # make duplicate detection easier
        nums.sort()
        res = []
        used = [False] * len(nums)
        backtrack([], used)
        return res
