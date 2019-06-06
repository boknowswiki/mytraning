#!/usr/bin/python -t

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res=[0]
        while len(res)<=num:
            res+=[i+1 for i in res]
        return res[:num+1]

#myself
#time O(n) space O(n)
#for num:
#0, 1, \\ 2, 3, \\ 4, 5, 6, 7, \\ 8, 9, 10, 11, 12, 13, 14, 15, \\16
#number of bits:
#0, 1, \\ 1, 2, \\ 1, 2, 3, 3, \\ 1, 2, 2, 3, 2, 3, 3, 4, \\ 1
#l[i] = l[index] + 1 index from 0 when i hit power of 2.

#here is a better one, from https://leetcode.com/problems/counting-bits/discuss/79557/How-we-handle-this-question-on-interview-Thinking-process-%2B-DP-solution
#dp[index] = dp[index - offset] + 1;

import math
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def ispowerof2(n):
            return n != 0 and (n & (n-1) == 0)
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        
        l = [0] *(num+1)
        l[0] = 0
        l[1] = 1
        index = 0
        
        for i in range(2, num+1):
            if ispowerof2(i):
                index = 0
                l[i] = 1
                
            l[i] = l[index] + 1
            index += 1
            
        return l

'''
#myself
#time O(n*sizeof(integer)) space O(n)

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def get_num_bit(i):
            cnt = 0
            while i:
                if i & 1:
                    cnt += 1
                i >>= 1
                
            return cnt
            
        ret = []
        
        for i in range(num+1):
            ret.append(get_num_bit(i))
            
        return ret
'''
if __name__ =='__main__':
    ss = Solution()
    print('answer is %s' % str(ss.countBits(8)))