#!/usr/bin/python -t

# 采用算法强化班中讲到的单调栈。
# 要做这个题之前先做直方图最大矩阵（Largest Rectangle in Histogram） 这个题。
# 这个题其实就是包了一层皮而已。一行一行的计算以当前行为矩阵的下边界时，最大矩阵是什么。
# 计算某一行为下边界时的情况，就可以转换为直方图最大矩阵问题了。

class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        if not matrix:
            return 0
            
        heights = [0] * len(matrix[0])
        ret = 0
        
        for row in matrix:
            for index, val in enumerate(row):
                heights[index] = heights[index]+1 if val else 0
                #print heights
            ret = max(ret, self.find_max_area(heights))
                
        return ret
        
    def find_max_area(self, heights):
        n = len(heights)
        ret = 0
        
        if n == 0:
            return ret
        
        st = []
        
        for i in range(n+1):
            cur = heights[i] if i != n else -1
            
            while len(st) != 0 and heights[st[-1]] >= cur:
                h = heights[st.pop()]
                w = i if len(st) == 0 else i-st[-1]-1
                ret = max(ret, w*h)
            st.append(i)
            
        return ret
        
