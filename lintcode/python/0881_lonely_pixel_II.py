#!/usr/bin/python -t


import collections

class Solution:
    """
    @param picture: a 2D char array
    @param N: an integer
    @return: return a integer
    """
    def findBlackPixel(self, picture, N):
        # write your code here
        r, c = len(picture), len(picture[0])
        rows, cols = [0] * r, [0] * c
        for i in range(r):
            for j in range(c):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1

        sdict = collections.defaultdict(int)
        for idx, row in enumerate(picture):
            sdict[''.join(row)] += 1

        ret = 0
        for i in range(r):
            row = ''.join(picture[i])
            if sdict[row] != N:
                continue
            for j in range(c):
                if picture[i][j] == 'B':
                    if rows[i] == N and cols[j] == N:
                            ret += 1
        return ret
