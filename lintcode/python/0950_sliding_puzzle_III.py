#!/usr/bin/python -t


import collections

class Solution:
    """
    @param matrix: The 3*3 matrix
    @return: The answer
    """
    def  jigsawPuzzle(self, matrix):
        # Write your code here
        start, end = "", "123456780"
        
        for i in range(3):
            for j in range(3):
                start += str(matrix[i][j])
                
        v, q = set(start), collections.deque([start])
        
        while q:
            cur = q.popleft()
            if cur == end:
                return "YES"
            for nxt in self.getNext(cur):
                if nxt not in v:
                    v.add(nxt)
                    q.append(nxt)
                    
        return "NO"
        
    def getNext(self, cur):
        nxts = []
        zero_pos = cur.find("0")
        x, y = zero_pos/3, zero_pos%3

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx = dx+x
            ny = dy+y
            
            if 0 <= nx < 3 and 0 <= ny < 3:
                zero = 3 * x + y
                change = 3 * nx + ny
                
                nxt = cur[:zero] + cur[change] + cur[zero+1:]
                nxt = nxt[:change] + "0" + nxt[change+1:]
                nxts.append(nxt)
                
        return nxts
