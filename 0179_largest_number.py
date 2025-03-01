from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert to strings
        nums_str = list(map(str, nums))

        # Define a custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        # Sort the list using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))

        # Handle the case where the largest number is "0"
        if nums_str[0] == "0":
            return "0"

        return "".join(nums_str)
