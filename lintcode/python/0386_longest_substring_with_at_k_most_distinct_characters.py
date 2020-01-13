#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        n = len(s)
        if n <= k:
            return n
            
        left = 0
        right = 0
        ret = 0
        cnt = {}
        
        for right in range(n):
            cnt[s[right]] = cnt.get(s[right], 0) + 1
            while left <= right and len(cnt) > k:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            ret = max(ret, right-left+1)
            
        return ret
        
