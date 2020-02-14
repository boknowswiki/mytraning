#!/usr/bin/python -t

# heap


import heapq

class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        m = len(matrix)
        n = len(matrix[0])
        
        v = set()
        min_heap = [(matrix[0][0], 0, 0)]
        v.add((0, 0))
        ret = 0
        dx = [0, 1]
        dy = [1, 0]
        
        for _ in range(k):
            ret, x, y = heapq.heappop(min_heap)
            for j in range(2):
                cx = x + dx[j]
                cy = y + dy[j]
                if cx < m and cy < n and (cx, cy) not in v:
                    heapq.heappush(min_heap, (matrix[cx][cy], cx, cy))
                    v.add((cx, cy))
                    
        return ret
        
