class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a={"q","w","e","r","t","y","u","i","o","p"}
        b={"a","s","d","f","g","h","j","k","l"}
        c={"z","x","c","v","b","n","m"}
        res=[]
        for w in words:
            s=set([item.lower() for item in w])
            if s<=a or s<=b or s<=c: # issubset
                res.append(w)
        return res