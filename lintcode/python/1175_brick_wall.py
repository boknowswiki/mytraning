#!/usr/bin/python -t

# hash table and presum

class Solution:
    """
    @param wall: a list of rows
    @return: the number of crossed bricks
    """
    def leastBricks(self, wall):
        # write your code here
        n = len(wall)
        pre_sum = {}
        
        for i in range(n):
            row = wall[i]
            val = 0
            for j in row:
                val += j
                pre_sum[val] = pre_sum.get(val, 0) + 1
                
        #print pre_sum
                
        max_cnt = 0
        for k in pre_sum:
            if pre_sum[k] > max_cnt and pre_sum[k] != n:
                max_cnt = pre_sum[k]
                
        #print max_cnt
                
        return n-max_cnt
        
