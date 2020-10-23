#!/usr/bin/python -t


import sys
#fromt collections import deque

class Solution:
    """
    @param board: the given board
    @return:  the least number of moves required so that the state of the board is solved
    """
    def slidingPuzzle(self, board):
        # write your code here
        if not board or not board[0]:
            return -1
        
        m = len(board)
        n = len(board[0])
        org = ""
        for i in range(m):
            for j in range(n):
                org += str(board[i][j])
                
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        
        q = []
        q.append(org)
        v = set()
        v.add(org)
        ret = 0
        
        while q:
            l = len(q)
            for _ in range(l):
                b = q.pop(0)
                if b == "123450":
                    return ret
                
                index = b.index("0")
                x = index//3
                y = index%3
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n:
                        new_index = nx*3 + ny
                        min_index = min(new_index, index)
                        max_index = max(new_index, index)
                        new_b = b[:min_index] + b[max_index] + b[min_index+1:max_index] + b[min_index] + b[max_index+1:]
                        if new_b not in v:
                            v.add(new_b)
                            q.append(new_b)
            ret += 1
            
        return -1
