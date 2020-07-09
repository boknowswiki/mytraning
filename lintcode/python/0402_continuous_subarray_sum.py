#!/usr/bin/python -t

# subarray

# 枚举即可, 枚举的过程中维护以当前元素结尾的最大和.
# 
# 每次循环把当前元素加到这个和中, 在加上之前判断:
# 
# 如果这个和是负数, 则放弃之前的元素, 把和置为0, 区间左端点设为当前元素
# 如果是正数, 则直接累加.
# 同时, 在枚举的过程中维护答案.

class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        # write your code here
        ret = [-1, -1]
        left = 0
        right = -1
        total = 0
        max_sofar = -sys.maxint
        
        for a in A:
            #print a, total, max_sofar, left, right
            
            if total < 0:
                total = a
                left = right+1
                right = left
            else:
                total += a
                right += 1
            if total > max_sofar:
                max_sofar = total
                ret = [left, right]
                
        return ret

        
