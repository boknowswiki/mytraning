#!/usr/bin/python -t

# binar search
#用二分法求解。
#用一个数组维护所有区间的起始点，那么对于一个区间，它的右区间只需要找出大于或等于它的右边界的值即可，
#那么对于起始点构成的数组如果有序则可以直接二分查找。

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: a list of intervals
    @return: return a list of integers
    """
    def findRightInterval(self, intervals):
        # write your code here
        ret = [-1] * len(intervals)
        l = [(intervals[i], i) for i in range(len(intervals))]
        l.sort(key=lambda x: x[0].start)
        
        for i in range(len(l)):
            u = l[i][0]
            left = i+1
            right = len(l) -1
            
            while left < right:
                mid = left + (right-left)/2
                if l[mid][0].start < u.end:
                    left = mid+1
                else:
                    right = mid
            ret[l[i][1]] = l[left][1] if left < len(l) and l[left][0].start >= u.end else -1
        return ret

