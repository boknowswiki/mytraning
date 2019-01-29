#!/usr/bin/python -t

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        j = -1
        max_len = 0

        for k in range(1, n):
            if s[k] == s[k-1]:
                continue
            if j >= 0 and s[j] != s[k]:
                max_len = max(max_len, k-i)
                i = j + 1 
            j = k - 1

        return max(max_len, n-i)


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        l = [0]*256
        max_len = 0
        i = 0
        num_dist = 0

        for j in range(n):
            if l[ord(s[j])] == 0:
                num_dist = num_dist + 1

            l[ord(s[j])] = l[ord(s[j])] + 1

            while num_dist > 2:
                l[ord(s[i])] = l[ord(s[i])] - 1
                if l[ord(s[i])] == 0:
                    num_dist = num_dist - 1
                i = i + 1

            max_len = max(max_len, j-i+1)

        return max_len


