class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m=Counter(magazine)

        for ch in ransomNote:
            if m[ch]==0:
                return False
            m[ch]-=1
        
        return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))