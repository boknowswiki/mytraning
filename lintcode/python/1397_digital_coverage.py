#!/usr/bin/python -t

# sweep line

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: The intervals
    @return: The answer
    """
    def digitalCoverage(self, intervals):
        # Write your code here
        n = 0
        for interval in intervals:
            n = max(n, interval.end)
        dist = [0 for i in range(n + 2)]
        for interval in intervals:
            dist[interval.start] += 1
            dist[interval.end + 1] -= 1
        ansIdx = 0
        ansSum = 0
        sum = 0
        for i in range(1, n + 1):
            sum += dist[i]
            if sum > ansSum:
                ansIdx = i
                ansSum = sum
        return ansIdx


class Solution:
    """
    @param intervals: The intervals
    @return: The answer
    """
    def digitalCoverage(self, intervals):
        # Write your code here
        events = []
        for interval in intervals:
            events.append((interval.start,-1))
            events.append((interval.end,1))
        
        events.sort()

        max_count = 0
        count = 0
        

        for node,check in events:
            if check == -1:
                count+=1
            else:
                count-=1
            if count>max_count:
                max_count = count
                res = node

        return res
