#!/usr/bin/python -t

# binary search solution


import bisect

class WebLogger:
    
    def __init__(self):
        # do intialization if necessary
        self.q = []

    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        # write your code here
        self.q.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        # write your code here
        if not self.q:
            return 0
            
        n = len(self.q)
        
        #index = bisect.bisect(self.q, timestamp-300)
        index = self.upper_bound(self.q, timestamp-300)
            

        return len(self.q) - index
       
    def upper_bound(self, q, target):
        n = len(q)
        l = 0
        r = n
        while l < r:
            mid = (l+r)/2
            if q[mid] <= target:
                l = mid+1
            else:
                r = mid
        return l


class WebLogger:
    
    def __init__(self):
        # do intialization if necessary
        self.q = []

    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        # write your code here
        self.q.append(timestamp)

    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        # write your code here
        if not self.q:
            return 0
            
        n = len(self.q)
        
        i = 0
        while i < n and self.q[i] + 300 <= timestamp:
            i += 1
            
        self.q = self.q[i:]
        return self.q
       

