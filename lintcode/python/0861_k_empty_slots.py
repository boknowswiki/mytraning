#!/usr/bin/python -t

# 考点：
# 
# 贪心
# 题解：
# days[i]表示i位置花开放的时间，首先找到区间最早开的花，判断条件days[i] < days[left] or days[i] <= days[right]，表示当前i开放的时间较早，就继续将left=i，r=i+k+1，将较早开放的花作为区间左端点。i == right，表示当前区间左右端点是区间最早开放的， res = min(res, max(days[left], days[right])) 左右两端点为区间最早开放的两朵花，选择较晚开放的，更新最小答案。

class Solution:
    """
    @param flowers: the place where the flower will open in that day
    @param k:  an integer
    @return: in which day meet the requirements
    """
    def kEmptySlots(self, flowers, k):
        # Write your code here
        n = len(flowers)
        position = [0]*(n+1)
        for i in range(n):
            position[flowers[i]] = i
        
        ret = float("inf")
        lo = 1
        hi = k + 2
        i = 1
        while hi <= n:
            if position[i]>position[lo] and position[i]>position[hi]:
                i += 1
                continue
            if i==hi: ret = min(ret, max(position[lo], position[hi])+1)
            lo = i
            hi = i + k + 1
            i += 1
        if ret==float("inf"): return -1
        else: return ret
