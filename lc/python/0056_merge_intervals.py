# array and sorting
# time O(nlogn)
# space O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 2:
            return intervals

        ret = []

        intervals.sort(key=lambda x: x[0])
        for i in range(n):
            if not ret:
                ret.append(intervals[i])
                continue
            if ret[-1][1] >= intervals[i][0]:
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
                continue
            ret.append(intervals[i])
            
 
        return ret


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
