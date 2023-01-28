# hash map and sliding windows

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or n <= k:
            return n

        l = 0
        w = dict()
        ret = 0

        for r in range(n):
            w[s[r]] = w.get(s[r], 0) + 1
            while len(w) > k:
                w[s[l]] -= 1
                if w[s[l]] == 0:
                    del w[s[l]]
                l += 1

            ret = max(ret, r-l+1)

        return ret
