#!/usr/bin/python -t

# heap
# 利用堆求第k大元素


import heapq

class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        # write your code here
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                ret = heapq.heappop(heap)
                #print ret
                
        ret = heapq.heappop(heap)
            
        return ret
        
        
