class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        m = len(board[0])

        for i in range(n):
            uniqueX = set()
            uniqueY = set()
            for j in range(m):
                    if board[i][j] in uniqueX:
                        return False
                    if board[j][i] in uniqueY:
                        return False
                    if board[i][j] != '.':
                        uniqueX.add(board[i][j])
                    if board[j][i] != '.':
                        uniqueY.add(board[j][i])
        
        for square in range(n):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
                



                

        