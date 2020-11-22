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
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        if not list1:
            return list2
        if not list2:
            return list1
            
        m = len(list1)
        n = len(list2)
        i = j = 0
        ret = []
        
        while i < m and j < n:
            if list1[i].start <= list2[j].start:
                self.merge(ret, list1[i])
                i += 1
            else:
                self.merge(ret, list2[j])
                j += 1
                
        while i < m:
            self.merge(ret, list1[i])
            i += 1
            
        while j < n:
            self.merge(ret, list2[j])
            j += 1
            
        return ret
        
    def merge(self, ret, interval):
        if not ret:
            ret.append(interval)
            return
        
        if ret[-1].end < interval.start:
            ret.append(interval)
        else:
            ret[-1].end = max(ret[-1].end, interval.end)
            
        return
