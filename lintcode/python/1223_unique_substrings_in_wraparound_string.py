#!/usr/bin/python -t

# dp solution time O(n) space O(n)

class Solution:
    """
    @param p: the given string
    @return: the number of different non-empty substrings of p in the string s
    """
    def findSubstringInWraproundString(self, p):
        # Write your code here
        if p is None or len(p) == 0: return 0
        d = {p[0]: 1}
        last = p[0]
        count = 1
        for c in p[1:]:
            if ord(c) == ord(last) + 1 or c == 'a' and last == 'z': count += 1
            else: count = 1
            last = c
            if c in d: d[c] = max(d[c], count)
            else: d[c] = count
        return sum(d.values())


class Solution:
    """
    @param p: the given string
    @return: the number of different non-empty substrings of p in the string s
    """
    def findSubstringInWraproundString(self, p):
        # Write your code here
        # dp[i] the number of different non-empty substrings of p in s at letter i
        # dp[i] = 1
        # ret = sum(dp[i])
        
        dp = {i:1 for i in p}
        l = 1
        for i, j in zip(p, p[1:]):
            l = l+1 if (ord(j)-ord(i))%26 == 1 else 1
            dp[j] = max(dp[j], l)
            
        return sum(dp.values())


