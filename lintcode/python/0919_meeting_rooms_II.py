#!/usr/bin/python -t

# heap

# 先对intervals 按照 start 排序。之后建立一个PriorityQueue用来记录end。
# 遍历intervals时，每一个interval的start如果和最小的end有冲突（PriorityQueue会自动poll最小的end），
# 说明需要新的会议室，把这一个end加入队列。
# 如果和最小的end没有冲突，可以把最小的end poll（）走，因为新的end取决于当前interval的end。
# 最后队列元素的个数就是需要会议室的数目。
# 
# 因为排过序，时间复杂度应该是 O（nlogn）。空间复杂度需要一个队列，应该是O（n）


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
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        intervals = sorted(intervals, key=lambda i : i.start)
        #print intervals
        
        heap = []
        heapq.heappush(heap, intervals[0].end)
        
        for i in range(1, len(intervals)):
            if heap[0] < intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            
        return len(heap)


# 使用九章算法强化班中讲到的扫描线算法
# 房间的开始/结束 时间排个序
# 每次开始一个房间 就room++
# 然后每次开新房判断之前的房间结束没有 之前房间结束就不用开新房了
# time O(nlogn) space O(n)


        

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        points = []
        for i in intervals:
            points.append((i.start, 1))
            points.append((i.end, -1))
            
        ongoing_meeting = 0
        ret = 0
        
        for p in sorted(points):
            ongoing_meeting += p[1]
            ret = max(ret, ongoing_meeting)
            
        return ret
        
        
            
