#!/usr/bin/python -t

# heap
# 使用 Heapq 的方法
# 最快，因为不需要创建额外空间。
# 时间复杂度和其他的算法一致，都是 
# O(NlogK) N 是所有元素个数


import heapq

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        ret = []
        heap = []
        
        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heapq.heappush(heap, (array[0], index, 0))
            
        while len(heap):
            val, x, y = heapq.heappop(heap)
            ret.append(val)
            if y + 1 < len(arrays[x]):
                heapq.heappush(heap, (arrays[x][y+1], x, y+1))
                
        return ret
        

# divid and conqur


class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        n = len(arrays)
        
        return self.helper(arrays, 0, n-1)
        
    def helper(self, arrays, start, end):
        if start >= end:
            return arrays[start]
            
        mid = (start + end) /2
        
        left = self.helper(arrays, start, mid)
        right = self.helper(arrays, mid+1, end)
        
        return self.merge(left, right)
        
    def merge(self, l1, l2):
        ret = []
        
        len_l1 = len(l1)
        index1 = 0
        len_l2 = len(l2)
        index2 = 0
        
        while index1 < len_l1 and index2 < len_l2:
            if l1[index1] < l2[index2]:
                ret.append(l1[index1])
                index1 += 1
            else:
                ret.append(l2[index2])
                index2 += 1
                
        if index1 < len_l1:
            ret.extend(l1[index1:])
        if index2 < len_l2:
            ret.extend(l2[index2:])
            
        return ret
        
