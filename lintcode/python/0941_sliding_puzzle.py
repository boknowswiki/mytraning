#!/usr/bin/python -t

# bfs

import collections

class Solution:
    """
    @param board: the given board
    @return:  the least number of moves required so that the state of the board is solved
    """
    def slidingPuzzle(self, board):
        # write your code here
        boardStr = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardStr += str(board[i][j])

        #print(boardStr)
        expectStr = "123450"
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
                    if 0 <= nx < 2 and 0 <= ny < 3:
                        minIndex = min(nx*3+ny, zeroIndex)
                        maxIndex = max(nx*3+ny, zeroIndex)
                        nextBoard = curBoard[:minIndex] + curBoard[maxIndex] + curBoard[minIndex+1:maxIndex] + curBoard[minIndex]+ curBoard[maxIndex+1:]
                        if nextBoard not in v:
                            v.add(nextBoard)
                            q.append(nextBoard)

            ret += 1

        return -1

if __name__ == '__main__':
    s = Solution()
    a= [[1,2,3],[4,0,5]]
    print(s.slidingPuzzle(a))