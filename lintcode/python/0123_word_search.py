#!/usr/bin/python -t

# dfs and backtracking

class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        m = len(board)
        if m == 0:
            return False
            
        n = len(board[0])
        if n == 0:
            return False
        v = set()
        
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j, m, n, v):
                    return True
                    
        return False
        
    def dfs(self, board, word, x, y, m, n, v):
        if word == '':
            return True
        if x < 0 or x >= m or y < 0 or y >=n:
            return False
        
        if word[0] == board[x][y] and (x, y) not in v:
            v.add((x, y))
            if self.dfs(board, word[1:], x+1, y, m, n, v) or self.dfs(board, word[1:], x-1, y, m, n, v) or \
                self.dfs(board, word[1:], x, y+1, m, n, v) or self.dfs(board, word[1:], x, y-1, m, n, v):
                    return True
            else:
                v.remove((x, y))
                
        return False
