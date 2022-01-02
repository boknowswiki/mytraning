#!/usr/bin/python -t

# queue & sliding window & data stream

import collections

class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.hq = collections.deque([])
        self.total = 0


    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        self.total += val
        self.hq.append(val)
        if len(self.hq) > self.size:
            remove_val = self.hq.popleft()
            self.total -= remove_val

        return self.total/len(self.hq)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
