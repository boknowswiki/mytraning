#!/usr/bin/python -t

class Solution:
    """
    @param Events: the start and end time
    @return: if there has a solution return 1, otherwise return -1.
    """
    def CheerAll(self, Events):
        # write your code here
        Events.sort(key = lambda x:x[1] - (x[1] - x[0]) / 2 - 1)
        
        time = 0
        for event in Events:
            start = event[0]
            end = event[1]
            duration = (event[1] - event[0]) / 2 + 1
            time = max(time, start)
            if end - time < duration:
                return -1
            time += duration
           
        return 1
