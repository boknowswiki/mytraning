#!/usr/bin/python -t

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        intervals.sort(key=lambda x: x.start)
        #print intervals
        
        n = len(intervals)
        ret = []
        
        for i in range(n):
            if len(ret) == 0 or ret[-1].end < intervals[i].start:
                ret.append(intervals[i])
            else:
                ret[-1].end = max(ret[-1].end, intervals[i].end)
                
        return ret

