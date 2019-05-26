#!/usr/bin/python -t

#set O(1) get O(logn) space O(n)

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.d[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        v = self.d.get(key, None)
        if v is None:
            return ""
        i = bisect.bisect(v, (timestamp, chr(127)))
        return v[i-1][1] if i else ""
        
