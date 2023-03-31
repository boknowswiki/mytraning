#!/usr/bin/python -t

# heap

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        v = set()
        if m == 0 or n == 0:
            return 0

        hq = [(matrix[0][0], 0, 0)]
        v.add((0, 0))

        while hq and k > 1:
            _, i, j = heapq.heappop(hq)
            if i + 1 < m and (i+1, j) not in v:
                v.add((i+1, j))
                heapq.heappush(hq, (matrix[i+1][j], i+1, j))
            if j + 1 < n and (i, j+1) not in v:
                v.add((i, j+1))
                heapq.heappush(hq, (matrix[i][j+1], i, j+1))

            k -= 1

        return hq[0][0]

# binary search
#time O(nlogn) space O(1)
'''

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = matrix[0][0]
        r = matrix[-1][-1]
        
        while l < r:
            m = l + (r-l)/2
            if sum(bisect.bisect_right(row, m) for row in matrix) < k:
                l = m+1
            else:
                r = m
        return l

'''

import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        print heap
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            print ret, i, j, heap
            if j+1 < len(matrix[0]):
                print matrix[i][j+1], i, j+1
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
                print heap
        return ret

'''
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], k = 8, return = 13
'''

if __name__ == '__main__':
    m = [[ 1,  5,  9],
                [10, 11, 13],
                [12, 13, 15]
        ]
    k = 8
    #return = 13

    s = Solution()
    print "ret %d" % s.kthSmallest(m, k)
