class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need=Counter(t)
        window=defaultdict(int)

        required=len(need)
        formed=0

        ans=(float("inf"),None,None)

        l=0
        for r,ch in enumerate(s):
            window[ch]+=1

            if ch in need and window[ch]==need[ch]:
                formed+=1
            
            while l<=r and formed==required:
                ch2=s[l]

                if r-l+1<ans[0]:
                    ans=(r-l+1,l,r)
                
                window[ch2]-=1
                if ch2 in need and window[ch2]<need[ch2]:
                    formed-=1
                l+=1

        return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]