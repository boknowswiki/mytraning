#!/usr/bin/python -t

# hash table
# 数组记录每个技能之前一次的释放时间，然后对于当前技能，计算cd。

class Solution:
    """
    @param arr: The release order
    @param n: The cooldown
    @return: Return the time
    """
    def askForCoolingTime(self, arr, n):
        # Write your code here
        m = len(arr)
        d = {}
        ret = 0
        
        for i in range(m):
            if (arr[i] not in d) or (ret - d[arr[i]] >= n+1):
                ret += 1
            else:
                ret = d[arr[i]] + n + 1
            d[arr[i]] = ret
                
        return ret
        
