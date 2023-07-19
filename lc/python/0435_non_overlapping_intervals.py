# sort, greedy, dp
# time O(nlogn)
# space O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        ret = 0
        k = -inf

        for x, y in intervals:
            if x >= k:
                k = y
            else:
                ret += 1

        return ret
