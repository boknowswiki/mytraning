#!/usr/bin/python -t


# heap
# 使用 heap 来解决

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        heap = []
        ret = []
        
        for index, arrays in enumerate(intervals):
            if len(arrays) == 0:
                continue
            heapq.heappush(heap, (arrays[0].start, arrays[0].end, index, 0))
            
        while len(heap) > 0:
            start, end, index, col = heap[0]
            heapq.heappop(heap)
            self.append_and_merge(ret, Interval(start, end))
            if col+1 < len(intervals[index]):
                heapq.heappush(heap, (intervals[index][col+1].start, intervals[index][col+1].end, index, col+1))
                
        return ret
        
    def append_and_merge(self, ret, interval):
        if not ret:
            ret.append(interval)
            return
            
        last_interval = ret[-1]
        
        if last_interval.end < interval.start:
            ret.append(interval)
            return
        
        last_interval.end = max(last_interval.end, interval.end)
        
        return
    


# 先将所有元素拿出来按照start排个序，然后依次合并



# This reference program is provided by @jiuzhang.com
# Copyright is reserved. Please indicate the source for forwarding

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        arr = []
        for i in intervals:
            for j in i:
                arr.append(j)
        arr = sorted(arr, key=lambda o: o.start)
        ans = []
        if (len(arr) == 0) :
            return ans 
        ans.append(arr[0])
        for i in range(1, len(arr)):
            if (ans[len(ans) - 1].end >= arr[i].start):
                ans[len(ans) - 1].end = max(ans[len(ans) - 1].end, arr[i].end)
            else :
                ans.append(arr[i])
        return ans


