#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        n = len(s)
        left = right = 0
        ss = set()
        ret = 0
        
        for left in range(n):
            while right < n and s[right] not in ss:
                ss.add(s[right])
                right += 1
                
            ret = max(ret, right-left)
            ss.remove(s[left])
            
        return ret
        
        
