#!/usr/bin/python -t

# hash table and pre sum
# 前缀和：定义一个数组sum[N+1]，s[i]表示数组A中前i个元素之和，然后遍历sum数组，计算s[i]+S(含义：前i个元素之和是s[i],找和为S的子数组个数)。求s[i]+S的个数

class Solution:
    """
    @param A: an array
    @param S: the sum
    @return: the number of non-empty subarrays
    """
    def numSubarraysWithSum(self, A, S):
        # Write your code here.
        n = len(A)
        cnt = [0] * (n+1)
        ret = 0
        pre_sum = 0
        
        for i in range(n):
            pre_sum += A[i]
            if pre_sum >= S:
                ret += cnt[pre_sum-S]
            cnt[pre_sum] += 1
            
        return ret
        
