#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        if not n:
            return ""
            
        self.col = set()
        self.sum = set()
        self.diff = set()
        self.ret = []
        
        self.board = [[0] * n for _ in range(n)]
        
        self.dfs(0, n)
        
        return self.ret
        
    def dfs(self, row, n):
        if row == n:
            level = []
            for i in range(n):
                tmp = ""
                for j in range(n):
                    if self.board[i][j] == 0:
                        tmp += '.'
                    else:
                        tmp += 'Q'
                        
                level.append(tmp)
            self.ret.append(level)
            
        for i in range(n):
            if i not in self.col and (row+i) not in self.sum and (row-i) not in self.diff:
                self.col.add(i)
                self.sum.add(row+i)
                self.diff.add(row-i)
                self.board[row][i] = 1
                self.dfs(row+1, n)
                self.board[row][i] = 0
                self.col.remove(i)
                self.sum.remove(row+i)
                self.diff.remove(row-i)
                
        return
    
