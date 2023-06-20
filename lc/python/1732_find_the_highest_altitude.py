# array, prefix sum, presum
# time O(n)
# space O(1)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ret = 0
        total = 0

        for g in gain:
            total += g
            ret = max(ret, total)

        return ret
