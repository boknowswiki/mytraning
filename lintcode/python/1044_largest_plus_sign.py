#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n^2)

class Solution:
    """
    @param N: size of 2D grid
    @param mines: in the given list
    @return: the order of the plus sign
    """
    def orderOfLargestPlusSign(self, N, mines):
        # Write your code here
        up = [[0] * N for i in range(N)]
        down = [[0] * N for i in range(N)]
        left = [[0] * N for i in range(N)]
        right = [[0] * N for i in range(N)]
        
        d_mines = {(mine[0], mine[1]) for mine in mines}
        
        for i in range(N):
            for j in range(N):
                if (i, j) not in d_mines:
                    try:
                        left[i][j] = left[i][j-1]+1
                    except:
                        left[i][j] = 1
                    try:
                        down[i][j] = down[i-1][j]+1
                    except:
                        down[i][j] = 1
                        
        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                if (i, j) not in d_mines:
                    try:
                        up[i][j] = up[i+1][j] + 1
                    except:
                        up[i][j] = 1
                    try:
                        right[i][j] = right[i][j+1]+1
                    except:
                        right[i][j] = 1
                        
        ret = 0
        ret = max(min(up[i][j], down[i][j], left[i][j], right[i][j]) for i in range(N) for j in range(N))
        
        return ret

