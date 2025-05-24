class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        
        rows=['']*numRows
        cur_row=0
        go_down=False

        for c in s:
            rows[cur_row]+=c
            if cur_row==0 or cur_row==numRows-1:
                go_down= not go_down
            cur_row+=1 if go_down else -1
        
        return ''.join(rows)