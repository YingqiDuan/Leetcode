class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        l = len(flowerbed)
        
        while i < l and n > 0:
            if flowerbed[i] == 1:
                i += 2
                continue
            
            l_empty = (i == 0) or (flowerbed[i-1] == 0)
            r_empty = (i == l - 1) or (flowerbed[i+1] == 0)
            
            if l_empty and r_empty:
                flowerbed[i] = 1  
                n -= 1
                i += 2  
            else:
                i += 1
        
        return n <= 0
        
