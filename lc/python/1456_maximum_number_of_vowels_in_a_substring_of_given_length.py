# array, two pointers, sliding windows
# time O(n)
# space O(1)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {"a", "e", "i", "o", "u"}

        l = 0
        ret = 0
        cnt = 0

        for r in range(n):
            if s[r] in vowels:
                cnt += 1
            
            if l < r and r-l+1 > k:
                if s[l] in vowels:
                    cnt -= 1
                l += 1

            ret = max(ret, cnt)

        return ret
