from collections import Counter
def isAnagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

def isAnagram_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
