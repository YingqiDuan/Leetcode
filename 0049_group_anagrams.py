class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for s in strs:
            # Sort the string to use as a key
            so = "".join(sorted(s))
            if so not in m:
                m[so] = []
            m[so].append(s)

        return list(m.values())
