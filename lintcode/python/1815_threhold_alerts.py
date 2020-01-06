#!/usr/bin/python -t

# two pointers

class Solution:
    """
    @param n: 
    @param k: 
    @param l: is len 
    @param num: //same as problem
    @return: //return long
    """
    def solve(self, n, k, l, num):
        #
        times = 0
        val = 0
        val = 0
        
        for i in range(n):
            if i < l:
                val += num[i]
            else:
                val += num[i]
                val -= num[i-l]
                
            if i >= l-1 and val > k*l:
                times += 1
                
        return times
        
