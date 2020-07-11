#!/usr/bin/python -t

# subarray

# 分两种情况讨论：
# 
# 最大数组仍然是中间的某一段
# 最大数组是去掉了中间的一段之后剩下的部分
# 第一种情况用传统的最大子数组做法走一遍(参考题解)。第二种做法稍微想一下就可以证明中间被去掉的那一段是整个数组的 minimum subarray。
# 所以求一遍 minimum subarray 之后，比较两种情况, 取最优解即可
# 
# 需要特殊考虑 minimum subarray 是取了所有数的情况。

class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        # write your code here
        n = len(A)

        max_start, max_end, max_sum = self.find_max_sum(A)
        min_start, min_end, min_sum = self.find_max_sum([-i for i in A])
        min_sum = -min_sum
        
        if max_sum >= sum(A) - min_sum or min_end - min_start + 1 == n:
            return [max_start, max_end]
        
        return [min_end+1, min_start-1]
        
    def find_max_sum(self, s):
        max_sum = -sys.maxint
        max_cur = 0
        n = len(s)
        max_start = 0
        ret = []
        
        for i in range(n):
            if max_cur < 0:
                max_cur = 0
                max_start = i
            max_cur += s[i]
            if max_cur > max_sum:
                max_sum = max_cur
                ret = [max_start, i]
                
        return ret[0], ret[1], max_sum
