# two pointers

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
