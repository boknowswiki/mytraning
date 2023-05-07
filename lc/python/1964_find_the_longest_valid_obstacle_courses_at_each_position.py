# binary search, greedy
# time (nlogn)
# space O(n)

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ret = [1] * n

        l = []

        for i, h in enumerate(obstacles):
            idx = bisect.bisect_right(l, h)

            if idx == len(l):
                l.append(h)
            else:
                l[idx] = h

            ret[i] = idx+1

        return ret
