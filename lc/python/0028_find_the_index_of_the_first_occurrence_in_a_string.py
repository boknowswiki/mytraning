# two pointers

# time O(m+n)
# space O(m)

# kmp: https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[j] != needle[i]:
                j = pi[j - 1]
            if needle[j] == needle[i]:
                j += 1
            pi[i] = j
        j = 0
        for i in range(n):
            while j > 0 and needle[j] != haystack[i]:
                j = pi[j - 1]
            if needle[j] == haystack[i]:
                j += 1
            if j == m:
                return i - m + 1
        return -1

# time O(mn)
# space O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if m == 0 or m < n:
            return -1

        for i in range(m-n+1):
            j = 0
            if haystack[i] != needle[j]:
                continue
            else:
                j += 1
                while j < n:
                    if haystack[i+j] != needle[j]:
                        break
                    j += 1

                if j == n:
                    return i

        return -1
