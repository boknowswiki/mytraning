# hash map

class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.antidiag = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        val = 1 if player == 1 else -1

        self.row[row] += val
        self.col[col] += val

        if row == col:
            self.diag += val
        
        if col == self.n - row - 1:
            self.antidiag += val

        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag) == self.n or abs(self.antidiag) == self.n:
            return player
        
        return 0


        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
