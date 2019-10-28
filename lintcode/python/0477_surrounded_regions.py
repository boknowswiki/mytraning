#!/usr/bin/python -t

# BFS


from collections import deque

class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        if not board or (not board[0]):
            return
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            self.bfs(i, 0, board)
            self.bfs(i, n-1, board)
        
        for j in range(n):
            self.bfs(0, j, board)
            self.bfs(m-1, j, board)
        
        
        print board    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    
        return 
    
    def bfs(self, x, y, board):
        if board[x][y] != 'O':
            return
        #print "in bfs %d, %d" % (x, y)
        m = len(board)
        n = len(board[0])
        #print x, y
        q = deque()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        q.append((x,y))
        board[x][y] = 'T'
        
        while len(q) > 0:
            cx, cy = q.popleft()
            
            for i in range(4):
                nx = cx+dx[i]
                ny = cy+dy[i]
                if 0<=nx<m and 0<=ny<n and board[nx][ny] == 'O':
                    #print nx, ny
                    q.append((nx, ny))
                    board[nx][ny] = 'T'
                    
        return
    
            
