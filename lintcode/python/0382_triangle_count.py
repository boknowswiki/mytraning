#!/usr/bin/python -t

# two pointers

#使用双指针算法。
#for 循环最大边的位置 i，接下来的任务就是在 0~i-1 之间找到两数之和 > S[i]

class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        n = len(S)
        if n < 3:
            return 0
            
        S.sort()
        ret = 0
        
        for i in range(2, n):
            l = 0
            r = i-1
            while l < r:
                while l < r and S[l] + S[r] <= S[i]:
                    l += 1
                if l < r:
                    ret += r-l
                    
                r -= 1
                
        return ret
        
