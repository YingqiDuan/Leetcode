class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=set(nums)
        return [x for x in list(range(1,len(nums)+1)) if x not in n]