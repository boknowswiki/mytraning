#!/usr/bin/python -t

#time O(logs*log(len(t)) space O(len(t))

from collections import defaultdict
from bisect import bisect_left

class Solution(object):
    def creat_map(self, s):
        m = defaultdict(list)
        for i , char in enumerate(s):
            m[char].append(i)
        return m
    
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = self.creat_map(t)
        low_bound = 0
        
        for i in s:
            if i not in m:
                return False
            
            index_list = m[i]
            index = bisect_left(index_list, low_bound)
            if index == len(index_list):
                return False
            low_bound = index_list[index] + 1
            
        return True


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False
