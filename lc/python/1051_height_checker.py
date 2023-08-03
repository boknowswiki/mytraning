# sort, array
# time O(nlogn)
# space O(n)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = sorted(heights)

        ret = 0

        for a, b in zip(heights, arr):
            if a != b:
                ret += 1

        return ret
