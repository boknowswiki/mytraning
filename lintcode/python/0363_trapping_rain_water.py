#!/usr/bin/python -t

# two pointers
#使用九章算法班中讲过的相向型双指针算法。
#整个算法的思想是计算每个位置上可以盛放的水，累加起来。
#
#记录如下几个值：
#
#left, right => 左右指针的位置
#left_max, right_max => 从左到右和从右到左到 left, right 为止，找到的最大的 height
#每次比较 left_max 和 right_max，如果 left_max 比较小，就挪动 left 到 left + 1。
#与此同时，查看 left 这个位置上能够盛放多少水，这里有两种情况：
#
#一种是 left_max > heights[left]，这种情况下，水可以盛放 left_max - heights[left] 那么多。因为右边有 right_max 挡着，左侧可以到 left_max。
#一种是 left_max <= heights[left]，这种情况下，水无法盛放，会从左侧流走，此时更新 left_max 为 heights[left]
#left_max >= right_max 的情况类似处理。
#
#时间复杂度：O(n)
#空间复杂度 O(1)

class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        n = len(heights)
        if n == 0:
            return 0
        left, right = 0, n-1
        left_max, right_max = heights[left], heights[right]
        ret = 0
        
        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, heights[left])
                ret += left_max - heights[left]
                left += 1
            else:
                right_max = max(right_max, heights[right])
                ret += right_max - heights[right]
                right -= 1
                
        return ret
        
