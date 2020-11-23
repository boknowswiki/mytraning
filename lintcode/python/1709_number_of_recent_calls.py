#!/usr/bin/python -t

class RecentCounter(object):

    def __init__(self):
        self.l = []
        self.cnt = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.l.append(t)
        self.cnt += 1
        
        while self.l and self.l[0] < t-3000:
            del self.l[0]
            self.cnt -= 1
        
        return self.cnt
        
