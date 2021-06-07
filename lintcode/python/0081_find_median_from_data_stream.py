#!/usr/bin/python -t


# heap and stream data

import heapq

class Solution:
    def __init__(self):
        # do initialize if it is necessary
        self.max_heap = []
        self.min_heap = []
        self.is_first_add = True


    """
    @param val: An integer
    @return: nothing
    """
    def add(self, val):
        # write your code here
        if self.is_first_add:
            # 第一个进入数据流的数字是第一个中位数
            #self.median = val
            self.is_first_add = False
            heapq.heappush(self.max_heap, -val)
            self.median = -self.max_heap[0]
            return
    
        if val <= self.median:
            # 小的数放到大顶堆
            heapq.heappush(self.max_heap, -val)
        else:
            # 大的数放到小顶堆
            heapq.heappush(self.min_heap, val)

        # 比较堆中数字数量，调整堆和中位数
        if len(self.max_heap) > len(self.min_heap)+1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        self.median = -self.max_heap[0]
        return

    """
    @return: return the median of the data stream
    """
    def getMedian(self):
        # write your code here
        return self.median

#把比 median 小的放在 maxheap 里，把比 median 大的放在 minheap 里。median 单独放在一个变量里。
#每次新增一个数的时候，先根据比当前的 median 大还是小丢到对应的 heap 里。
#丢完以后，再处理左右两边的平衡性:
#
#如果左边太少了，就把 median 丢到左边，从右边拿一个最小的出来作为 median。
#如果右边太少了，就把 median 丢到右边，从左边拿一个最大的出来作为新的 median。
# heap
# time O(nlogn)

import heapq

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return []
        
        ret = []
        mid = nums[0]
        ret.append(mid)
        # num no more than mid
        max_hq = []
        # num more than mid
        min_hq = []
        
        for i in range(1, n):
            num = nums[i]
            if num < mid:
                heapq.heappush(max_hq, -num)
            else:
                heapq.heappush(min_hq, num)
            
            if len(max_hq) > len(min_hq):
                heapq.heappush(min_hq, mid)
                mid = -heapq.heappop(max_hq)
            elif len(max_hq) +1 < len(min_hq):
                heapq.heappush(max_hq, -mid)
                mid = heapq.heappop(min_hq)
                
            ret.append(mid)
            
        return ret
                
            
