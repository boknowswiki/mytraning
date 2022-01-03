#!/usr/bin/python -t

# sweep line and segment tree

# 扫描线 + 合并区间
# 首先把x1 y1 x2 y2变成 x1 y1 y2 1, x2 y1 y2 -1. 这一步的目的是对x做扫描线。 然后我们扫描的过程中， 去合并下y， 就能数出面积了。
# 
# 然后我们会有一个这个区间的intervals， 然后x变的时候， 就合并y去计算这个， 碰到1自然是加interval， 碰到-1就减去。

MOD = 1000000007

class Solution:
    """
    @param rectangles: type is List[List[int]]
    @return: return a integer number
    """
    def rectangleArea(self, rectangles):
        x_to_y_intervals = []
        for rectangle in rectangles:
            x_to_y_intervals.append((rectangle[0], rectangle[1], rectangle[3], 1))
            x_to_y_intervals.append((rectangle[2], rectangle[1], rectangle[3], -1))
        x_to_y_intervals.sort()

        last_x = -1
        curr_intervals = []
        answer = 0
        for x_to_y_interval in x_to_y_intervals:
            if x_to_y_interval[0] == last_x:
                self.add_interval(curr_intervals, x_to_y_interval)
            else:
                if last_x != -1:
                    merged_intervals = self.merge_intervals(curr_intervals)
                    answer += self.calculate_area(merged_intervals) * ((x_to_y_interval[0] - last_x) % MOD)
                    answer %= MOD
                last_x = x_to_y_interval[0]
                self.add_interval(curr_intervals, x_to_y_interval)
        merged_intervals = self.merge_intervals(curr_intervals)
        answer += self.calculate_area(merged_intervals) * (x_to_y_interval[0] - last_x)
        return answer

    def add_interval(self, intervals, interval):
        if interval[3] == 1:
            intervals.append((interval[1], interval[2]))
        else:
            for inter in intervals:
                if inter[0] == interval[1] and inter[1] == interval[2]:
                    intervals.remove(inter)
                    break

    def merge_intervals(self, intervals):
        intervals.sort()
        merged_intervals = []
        for interval in intervals:
            if not merged_intervals:
                merged_intervals.append(interval)
                continue
            if merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
                continue
            poped = merged_intervals.pop()
            merged_intervals.append((poped[0], max(interval[1], poped[1])))
        return merged_intervals

    def calculate_area(self, merged_intervals):
        answer = 0
        for interval in merged_intervals:
            answer += interval[1] - interval[0]
            answer %= MOD
        return answer
