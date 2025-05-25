class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        
        word_len=len(words[0])
        word_count=Counter(words)
        total_len=word_len*len(words)
        result=[]

        for i in range(word_len):
            l=i
            cur_count=Counter()
            for r in range(i,len(s)-word_len+1,word_len):
                word=s[r:r+word_len]
                if word in word_count:
                    cur_count[word]+=1
                    while cur_count[word]>word_count[word]:
                        l_word=s[l:l+word_len]
                        cur_count[l_word]-=1
                        l+=word_len
                    
                    if r+word_len-l==total_len:
                        result.append(l)
                else:
                    cur_count.clear()
                    l=r+word_len
        return result
