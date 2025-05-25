class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_i={}
        l=0
        max_l=0

        for r in range(len(s)):
            if s[r] in char_i and char_i[s[r]]>=l:
                l=char_i[s[r]]+1
            char_i[s[r]]=r
            max_l=max(max_l,r-l+1)
        return max_l