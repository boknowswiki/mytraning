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
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        n = len(intervals)
        ret = []
        
        intervals.sort(key=lambda x: x.start)
        
        for i in range(1, n):
            if intervals[i].start < intervals[i-1].end:
                return False

                
        return True
