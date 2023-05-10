#!/usr/bin/python -t

# matrix, array
# time O(n^2)
# space O(1)

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0]*n for _ in range(n)]

        left = up = 0
        right = n-1
        down = n-1
        idx = 1

        while idx <= n*n:
            # left to right
            for i in range(left, right+1):
                ret[up][i] = idx
                idx += 1

            # up to down
            for i in range(up+1, down+1):
                ret[i][right] = idx
                idx += 1

            # make sure on a different row
            if up != down:
                for i in range(right-1, left-1, -1):
                    ret[down][i] = idx
                    idx += 1

            # make sure on different col
            if left != right:
                for i in range(down-1, up, -1):
                    ret[i][left] = idx
                    idx += 1

            left += 1
            right -= 1
            up += 1
            down -= 1

        return ret

#time O(n) space O(1)

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return [[]]
        
        ret = [0] * (n)
        for i in range(n):
            ret[i] = [0] *(n)
        
        begin = 0
        end = n - 1
        num = 1
        
        while begin < end:
            for i in range(begin, end):
                ret[begin][i] = num
                num = num + 1
                
            for i in range(begin, end):
                ret[i][end] = num
                num = num + 1
            
            for i in range(end, begin, -1):
                ret[end][i] = num
                num = num + 1
                
            for i in range(end, begin, -1):
                ret[i][begin] = num
                num = num + 1
                
            begin = begin + 1
            end = end - 1
            
        if begin == end:
            ret[begin][begin] = num
              
        return ret


'''
Start with the empty matrix, add the numbers in reverse order until we added the number 1. Always rotate the matrix clockwise and add a top row:

    ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
                     |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
                                         |8 7|      |7 6 5|
'''

def generateMatrix(self, n):
    A, lo = [], n*n+1
    while lo > 1:
        lo, hi = lo - len(A), lo
        A = [range(lo, hi)] + zip(*A[::-1])
    return A
