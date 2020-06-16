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
        
        l_max = heights[0]
        r_max = heights[n-1]
        left = 1
        right = n-2
        ret = 0
        
        while left <= right:
            if l_max >= r_max:
                r_max = max(r_max, heights[right])
                ret += r_max - heights[right]
                right -= 1
            else:
                l_max = max(l_max, heights[left])
                ret += l_max - heights[left]
                left += 1
                
        return ret
        

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
        

# from https://blog.csdn.net/wzy_1988/article/details/17752809

# 首先，碰到这样的题目不要慌张，挨个分析每个A[i]能trapped water的容量，然后将所有的A[i]的trapped water容量相加即可
# 
# 其次，对于每个A[i]能trapped water的容量，取决于A[i]左右两边的高度（可延展）较小值与A[i]的差值，即volume[i] = [min(left[i], right[i]) - A[i]] * 1，这里的1是宽度，如果the width of each bar is 2,那就要乘以2了
# ————————————————
# 版权声明：本文为CSDN博主「低调小一」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/wzy_1988/java/article/details/17752809

# time O(n) space O(n)

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
            
        ret = 0
        
        left = [0] * n
        right = [0] * n
        
        left[0] = heights[0]
        l_max = heights[0]
        
        for i in range(1, n):
            if heights[i] > l_max:
                l_max = heights[i]
                
            left[i] = l_max
            
        print left
        
        right[n-1] = heights[n-1]
        r_max = heights[n-1]
        
        for j in range(n-2, -1, -1):
            if heights[j] > r_max:
                r_max = heights[j]
                
            right[j] = r_max
            
        print right
        
        for i in range(n):
            ret += min(left[i], right[i]) - heights[i]
            
        return ret
