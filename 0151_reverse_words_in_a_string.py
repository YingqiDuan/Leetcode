class Solution:
    def reverseWords(self, s: str) -> str:
        i = len(s) - 1
        res = ""

        while i >= 0:
            while i >= 0 and s[i] == " ":
                i -= 1
            if i < 0:
                break

            w = ""
            while i >= 0 and s[i] != " ":
                w = s[i] + w
                i -= 1

            if res:
                res += " "
            res += w
        return res
