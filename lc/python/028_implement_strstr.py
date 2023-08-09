#!/usr/bin/python -t

# array, sliding window
# time O(mn)
# space O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n > m:
            return -1
        if m == n:
            return 0 if haystack == needle else -1

        for i in range(m-n+1):
            j = 0
            while j < n and haystack[i+j] == needle[j]:
                j += 1

            if j == n:
                return i

        return -1

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)

        if n == 0:
            return 0
        
        if m == 0:
            return -1
        
        for i in range(m-n+1):
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    break
                if (j == n -1) and (haystack[i+j] == needle[j]):
                    return i
            
        return -1

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        if m == 0:
            return -1

        for i in range(m-n+1):
            for j in range(n):
                if haystack[i+j] == needle[j]:
                    continue
                else:
                    break
            if j == n - 1 and haystack[i+j] == needle[j]:
                return i

        return -1 
