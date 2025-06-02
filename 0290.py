class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(words)!=len(pattern):
            return False
        
        p2w,w2p={},{}
        for ch, w in zip(pattern,words):
            if ch in p2w and p2w[ch]!=w:
                return False
            if w in w2p and w2p[w]!=ch:
                return False
            
            p2w[ch]=w
            w2p[w]=ch
        return True

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return len(pattern) == len(words) and \
           [pattern.index(c) for c in pattern] == [words.index(w) for w in words]

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return (len(pattern) == len((words := s.split())) and len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words)))
