class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            t = strs[0][i]
            for s in strs[1:]:
                if len(s) - 1 < i or s[i] != t:
                    return strs[0][:i]
        return strs[0]
