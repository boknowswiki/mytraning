#!/usr/bin/python -t

# two pointers


class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        n = len(s)
        d = {}
        left = 0
        ret = 0
        
        for right in range(n):
            d[s[right]] = d.get(s[right], 0) + 1
            
            while left <= right and len(d) >= k:
                ret += n-right
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1
                    
        return ret
        
