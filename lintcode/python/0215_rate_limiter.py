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
