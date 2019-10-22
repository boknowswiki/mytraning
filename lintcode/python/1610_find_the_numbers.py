#!/usr/bin/python -t

#斐波那契数列数列即f[i] = f[i - 1] + f[i - 2],n不超过32bit即比n大一点小一点不会超过32bit，for循环一遍遍历，时间复杂度也不会超过3s

class Solution:
    """
    @param n: the integer
    @return: the numbers that larger and smaller than `n` 
    """
    def getNumbers(self, n):
        # Write your code here
        if n < 0:
            return []
        if n == 0:
            return [1]
            
        cur = 0
        a, b = 0, 1
        
        while cur < n:
            a, b = b, a+b
            cur = b
            
        if cur == n:
            return [a, a+cur]
        else:
            return [a, cur]
            

