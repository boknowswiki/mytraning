#!/usr/bin/python -t

# two pointers
# O(n) 时间复杂度。双指针，发现局部最低点，则更新左指针。 另外，相邻相等的情况意味着没有峰值，所以也要更新左指针

class Solution:
    """
    @param A: 
    @return: the length of the longest mountain
    """
    def longestMountain(self, A):
        # write your code here
        n = len(A)
        left = 0
        ret = 0
        
        for right in range(n):
            if right > 1 and A[right-2] >= A[right-1] and A[right-1] < A[right]:
                left = right - 1
            if right > 1 and A[right-1] == A[right]:
                left = right
                
            ret = max(ret, right-left+1)
            
        return ret
        

# 统计当前上升或者下降状态的长度，并计算出其中最长的长度

class Solution:
    """
    @param A: 
    @return: the length of the longest mountain
    """
    def longestMountain(self, A):
        # write your code here
        n = len(A)
        up = down = ret = 0
        
        for i in range(1, n):
            if down > 0 and A[i-1] < A[i] or A[i-1] == A[i]:
                up = down = 0
            if A[i-1] < A[i]:
                up += 1
            if A[i-1] > A[i]:
                down += 1
                
            if up > 0 and down > 0:
                ret = max(ret, up + down + 1)
                
        return ret
        
        
