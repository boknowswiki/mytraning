#!/usr/bin/python -t

# time O(n)

# 单调栈
# 题解：
# 用九章算法强化班中讲过的单调栈(stack)。维护一个单调递增栈，逐个将元素 push 到栈里。push 进去之前先把 >= 自己的元素 pop 出来。
# 每次从栈中 pop 出一个数的时候，就找到了往左数比它小的第一个数（当前栈顶）和往右数比它小的第一个数（即将入栈的数），
# 从而可以计算出这两个数中间的部分宽度 * 被pop出的数，就是以这个被pop出来的数为最低的那个直方向两边展开的最大矩阵面积。
# 因为要计算两个数中间的宽度，因此放在 stack 里的是每个数的下标。

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if not height:
            return 0
            
        n = len(height)
        ret = 0
        st = []
        
        for i in range(n+1):
            #print "i is ", i
            cur = -1 if i == n else height[i]
            while len(st) != 0 and height[st[-1]] >= cur:
                #print st, cur
                h = height[st.pop()]
                w = i if len(st) == 0 else i-st[-1]-1
                ret = max(ret, h*w)
                #print ret
            
            st.append(i)
                
        return ret
        
