class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])

        dir = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for i in range(m):
            for j in range(n):
                nbr = 0
                for dx, dy in dir:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        nbr += board[ni][nj] & 1
                old = board[i][j] & 1
                new = 0
                if old == 1 and (nbr == 2 or nbr == 3):
                    new = 1
                if old == 0 and nbr == 3:
                    new = 1
                board[i][j] |= new << 1

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
