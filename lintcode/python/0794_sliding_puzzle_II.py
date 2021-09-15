#!/usr/bin/python -t

# bfs

import collections

class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # # write your code here
        start = self.toString(init_state)
        end = self.toString(final_state)
        q = collections.deque([start])
        v = set()
        v.add(start)
        ret = 0

        while q:
            l = len(q)
            
            for _ in range(l):
                p = q.popleft()
                if p == end:
                    return ret
                for nxt in self.getNext(p):
                    if nxt not in v:
                        q.append(nxt)
                        v.add(nxt)
            ret += 1

        return -1

    def toString(self, a):
        nxt = ['0']*9
        for i in range(3):
            for j in range(3):
                nxt[i*3+j] = str(a[i][j])

        return ''.join(nxt)

    def getNext(self, a):
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        nexts = []
        startIndex = a.index('0')
        x = startIndex//3
        y = startIndex%3

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nxt = list(a)
                nxt[startIndex] = a[nx*3+ny]
                nxt[nx*3+ny] = '0'
                nexts.append(''.join(nxt))

        return nexts

