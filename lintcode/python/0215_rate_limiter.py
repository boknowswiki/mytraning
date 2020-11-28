#!/usr/bin/python -t


import collections
import bisect

class Solution:
    units = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}

    def __init__(self):
        self.events = collections.defaultdict(list)
        
    # @param {int} timestamp the current timestamp
    # @param {string} event the string to distinct different event
    # @param {string} rate the format is [integer]/[s/m/h/d]
    # @param {boolean} increment whether we should increase the counter
    # @return {boolean} true of false to indicate the event is limited or not
    def isRatelimited(self, timestamp, event, rate, increment):
        limit, unit = rate.split('/')

        index = bisect.bisect_left(
            self.events[event], timestamp - self.units[unit] + 1)
        isLimited = len(self.events[event]) - index + 1 > int(limit)

        if not isLimited and increment:
            self.events[event].append(timestamp)

        return isLimited


# my version not AC, but should be correct.

class Solution:
    def __init__(self):
        self.d = {}
    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """
    def isRatelimited(self, timestamp, event, rate, increment):
        # write your code here
        split_index = rate.find("/")
        cnt = int(rate[:split_index])
        rate_type = rate[split_index+1:]
        
        time = 1
        if rate_type == "d":
            time = time * 60 * 60 * 24
        elif rate_type == "h":
            time = time * 60 * 60
        elif rate_type == "m":
            time = time * 60
            
        last_time = timestamp - time + 1
        
        if event not in self.d:
            self.d[event] = []
            
        #print self.d[event], timestamp
        index = self.find(self.d[event], last_time)
        print index
        block = len(self.d[event]) - index >= cnt
        if increment or not block:
            self.d[event].append(timestamp)
            
        return block
        
    def find(self, s, target):
        print s, target
        l = 0
        r = len(s) - 1
        if not s or s[r] < target:
            return len(s)
            
        while l + 1 < r:
            mid = l + (r-l)/2
            if s[mid] >= target:
                r = mid
            else:
                l = mid
                
        if s[l] >= target:
            return l
        if s[r] >= target:
            return r
        return len(s)
