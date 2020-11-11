#!/usr/bin/python -t

# https://www.jiuzhang.com/problem/sudoku-solver/

class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        # write your code here
        self.dfs(board, 0, 0)
        
        return
    
    def dfs(self, board, x, y):
        m, n = 9, 9
        if y == n:
            return self.dfs(board, x+1, 0)
        if x == m:
            return True
            
        if board[x][y] != 0:
            return self.dfs(board, x, y+1)
            
        for val in range(1, 10):
            if not self.valid(board, x, y, val):
                continue
            
            board[x][y] = val
            
            if self.dfs(board, x, y+1):
                return True
                
            board[x][y] = 0
            
        return False
                
    def valid(self, board, row, col, val):
        for i in range(9):
            if board[row][i] == val:
                return False

            if board[i][col] == val:
                return False
                
            if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == val:
                return False
                
        return True
