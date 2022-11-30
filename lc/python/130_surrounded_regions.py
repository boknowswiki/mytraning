#!/usr/bin/python -t

# dfs

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == "O":
                    self.dfs(board, m, n, i, j)
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == ".":
                    board[i][j] = "O"
                    
        return
    
    def dfs(self, board, m, n, x, y):
        board[x][y] = "."
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(dirs)):
            dx = x + dirs[i][0]
            dy = y + dirs[i][1]
            if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == "O":
                self.dfs(board, m, n, dx, dy)
                
        return

# bfs
# time O(m*n)
# space O(m*n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque([])
        
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == "O":
                    q.append((i, j))
                    board[i][j] = "."

                    
        while q:
            x, y = q.popleft()
            for i in range(len(dirs)):
                dx = dirs[i][0] + x
                dy = dirs[i][1] + y
                if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == "O":
                    board[dx][dy] = "."
                    q.append((dx, dy))
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == ".":
                    board[i][j] = "O"

#union find solution

class uf(object):
    def __init__(self, board):
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        self.father = [0] * (m*n+1)
        self.size = [1] * (m*n+1)
        
        for i in range(m):
            for j in range(n):
                index = i * n + j
                self.father[index] = index
                
        self.father[m*n] = m*n
        
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        
        if proot == qroot:
            return
        
        if self.size[proot] < self.size[qroot]:
            self.father[proot] = self.father[qroot]
            self.size[qroot] = self.size[qroot] + self.size[proot]
        else:
            self.father[qroot] = self.father[proot]
            self.size[proot] = self.size[proot] + self.size[qroot]
            
        return
        
    def find(self, p):
        tmp = p
        while p != self.father[p]:
            p = self.father[p]
        
        self.father[tmp] = p
        return p
        
    def connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        
        myuf = uf(board)
        
        for i in range(m):
            for j in range(n):
                if ((i == m - 1) or (i == 0) or (j == 0) or (j == n - 1)) \
                    and board[i][j] == 'O':
                    p = i * n + j
                    q = m*n
                    myuf.union(p, q)
                elif board[i][j] == 'O': 
                    p = i * n + j
                    
                    if i > 0 and board[i-1][j] == 'O':
                        q = p - n
                        myuf.union(p, q)
                    if j > 0 and board[i][j-1] == 'O':
                        q = p - 1
                        myuf.union(p, q)
                    if i < m - 1 and board[i+1][j] == 'O':
                        q = p + n
                        myuf.union(p, q)
                    if j < n - 1 and board[i][j+1] == 'O':
                        q = p + 1
                        myuf.union(p, q)
                        
        for i in range(m):
            for j in range(n):
                if not myuf.connected(i*n+j, m*n):
                    board[i][j] = 'X'
                    
        return
