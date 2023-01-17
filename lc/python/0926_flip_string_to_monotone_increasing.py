
# solutions from https://leetcode.com/problems/flip-string-to-monotone-increasing/solutions/2912351/flip-string-to-monotone-increasing/

# dp window
# time O(n)
# space O(1)

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m = 0
        for c in s:
            if c == '0':
                m += 1
        ans = m
        for c in s:
            if c == '0':
                m -= 1
                ans = min(ans, m)
            else:
                m += 1
        return ans
      
# dp
# time O(n)
# space O(1)

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = 0
        num = 0
        for c in s:
            if c == '0':
                ans = min(num, ans + 1)
            else:
                num += 1
        return ans
