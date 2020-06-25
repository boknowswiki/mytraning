#!/usr/bin/python -t

# sweep line
# 使用九章算法强化班中讲过的扫描线算法

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        cnts = []
        
        for airplane in airplanes:
            cnts.append([airplane.start, 1])
            cnts.append([airplane.end, 0])
            
        ret = cur = 0
        
        for _, start in sorted(cnts):
            if start == 1:
                cur += 1
            else:
                cur -= 1
                
            ret = max(ret, cur)
            
        return ret
