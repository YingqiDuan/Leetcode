class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        line=[]
        n=0

        for w in words:
            if n+len(w)+len(line)>maxWidth:
                for i in range(maxWidth-n):
                    line[i%(len(line)-1 or 1)]+=' '
                res.append(''.join(line))
                line,n=[],0
            
            line.append(w)
            n+=len(w)
        
        res.append(' '.join(line).ljust(maxWidth))
        return res