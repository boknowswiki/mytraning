# dfs and hash map

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rv = [[0]*n for _ in range(m)]
        cv = [[0]*n for _ in range(m)]
        subv = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] != ".":
                    val = ord(board[i][j]) - ord("0")-1
                    sub = i//3*3+j//3
                    #print(f"val {val}, i {i}, j {j}, sub {sub}")
                    if rv[i][val] or cv[val][j] or subv[sub][val]:
                        return False
                    rv[i][val] = cv[val][j] = subv[sub][val] = 1
                    
        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
