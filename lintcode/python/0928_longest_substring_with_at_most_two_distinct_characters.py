#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # Write your code here
        n = len(s)
        d = {}
        left = 0
        ret = 0
        
        for right in range(n):
            d[s[right]] = d.get(s[right], 0) + 1
            
            while left <= right and len(d) > 2:
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                    
                left += 1
                
            ret = max(ret, right-left+1)
            
        return ret
        
     
