#!/usr/bin/python -t

# two pointers
# 这题的正解因该是用双指针来维护一个虚拟的滑动窗口。说它是虚拟的是因为这个窗口大部分时间不连续。

# 窗口可以从尾部开始向右移动，也可以从头部开始向左移动。

class Solution:
    """
    @param list: The coins
    @param k: The k
    @return: The answer
    """
    def takeCoins(self, list, k):
        # Write your code here
        n = len(list)
        if n <= k:
            return sum(list)
            
        lo = -k
        hi = -1
        ret = running_coin = sum(list[lo:])
        
        while lo != 0:
            running_coin -= list[lo]
            lo += 1
            hi += 1
            running_coin += list[hi]
            
            ret = max(ret, running_coin)
            
        return ret
        
