# array
# time O(n)
# space O(1)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        for i in range(n):
            if intervals[i][1] < newInterval[0]:
                # current interval starts first & not covered by newInterval, add intervals[i] to ans
                # [curInterval]
                #                      [newInterval]
                ans.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                # newInterval starts first and not covered by current interval
                # Add newInterval to ans and set newInterval = curInterval
                #                       [curInterval]
                # [newInterval]
                ans.append(newInterval)
                newInterval = intervals[i]
            elif intervals[i][1] >= newInterval[0] or intervals[i][0] <= newInterval[1]:
                # They are overlapped, merge them
                # [curInterval]
                #        [newInterval]
                # or
                # [newInterval]
                #        [curInterval]
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        # add the last interval
        ans.append(newInterval) 
        return ans
