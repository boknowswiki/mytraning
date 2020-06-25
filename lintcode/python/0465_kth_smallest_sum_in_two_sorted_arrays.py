#!/usr/bin/python -t

# time klong(min(m,n,k))
# 类似于 Kth smallest in sorted matrix 一题。
# 使用 heapq
# 我们把行和列分别定为两个数组，就可以形成一个排好序的矩阵

import heapq

class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        m = len(A)
        n = len(B)
        if m == 0 or n == 0:
            return 0
            
        v = set((0, 0))
        ret = 0
        min_heap = [(A[0]+B[0], 0, 0)]
        
        for i in range(k):
            ret, index_a, index_b = heapq.heappop(min_heap)
            if index_b+1 < n and (index_a, index_b+1) not in v:
                heapq.heappush(min_heap, (A[index_a]+B[index_b+1], index_a, index_b+1))
                v.add((index_a, index_b+1))
            if index_a+1 < m and (index_a+1, index_b) not in v:
                heapq.heappush(min_heap, (A[index_a+1]+B[index_b], index_a+1, index_b))
                v.add((index_a+1, index_b))
                
        return ret
        
