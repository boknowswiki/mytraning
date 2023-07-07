# sliding window
# time O(n)
# space O(1)

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        v = collections.defaultdict(int)
        ret = 0
        l = 0

        for r in range(n):
            v[answerKey[r]] += 1

            while l <= r and v["T"] > k and v["F"] > k:
                v[answerKey[l]] -= 1
                l += 1

            ret = max(ret, r-l+1)

        return ret
