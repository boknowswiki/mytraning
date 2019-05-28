#!/usr/bin/python -t

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        l = sorted((e[0], i) for i, e in enumerate(intervals))
        ret = []
        
        for e in intervals:
            index = bisect.bisect_left(l, (e[1],))
            ret.append(l[index][1] if index < len(l) else -1)
            
        return ret
