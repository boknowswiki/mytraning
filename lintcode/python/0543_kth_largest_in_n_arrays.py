#!/usr/bin/python -t

# 使用 heapq
# heapq 是一个 maxheap，所以所有数取相反数往里丢。取出来的时候要再取一个相反数。

import heapq

class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        # write your code here
        n = len(arrays)
        if n == 0:
            return 0
            
        ret = 0
        k_heap = []
        
        for i in range(n):
            arrays[i].sort(reverse=True)
            #print arrays[i]
            
        for i in range(n):
            if arrays[i]:
                heapq.heappush(k_heap, (-1*arrays[i][0], i, 0))
                
        #print k_heap
        
        for _ in range(k):
            ret, a, index = heapq.heappop(k_heap)
            #print ret, a, index
            if index+1 < len(arrays[a]):
                heapq.heappush(k_heap, (-1 * arrays[a][index+1], a, index+1))
                    
        return -1 *ret

