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
        boardStr = ""
        for i in range(len(init_state)):
            for j in range(len(init_state[0])):
                boardStr += str(init_state[i][j])

        expectStr = ""
        for i in range(len(final_state)):
            for j in range(len(final_state[0])):
                expectStr += str(final_state[i][j])
        q = collections.deque([boardStr])
        v = set()
        v.add(boardStr)
        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        ret = 0

        while q:
            qLen = len(q)
            for _ in range(qLen):
                curBoard = q.popleft()

                if curBoard == expectStr:
                    return ret
                zeroIndex = curBoard.find('0')

                x = zeroIndex//3
                y = zeroIndex%3
                for i in range(len(dirs)):
                    nx = x + dirs[i][0]
                    ny = y + dirs[i][1]
                    #print(curBoard, nx, ny, zeroIndex)
                    if 0 <= nx < 3 and 0 <= ny < 3:
                        minIndex = min(nx*3+ny, zeroIndex)
                        maxIndex = max(nx*3+ny, zeroIndex)
                        nextBoard = curBoard[:minIndex] + curBoard[maxIndex] + curBoard[minIndex+1:maxIndex] + curBoard[minIndex]+ curBoard[maxIndex+1:]
                        if nextBoard not in v:
                            v.add(nextBoard)
                            q.append(nextBoard)

            ret += 1

        return -1
