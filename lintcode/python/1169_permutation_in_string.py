#!/usr/bin/python -t

# two pointers
# 先扫一遍字符串s1，统计各个字母的个数，取s2前s1长度个字符，匹配个数是否相符，若不相符，去除最前面的字符，加入后一个字符，重新比对，直至个数匹配，或扫描完s2。


import collections

class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def checkInclusion(self, s1, s2):
        # write your code here
        m = len(s1)
        d = collections.Counter(s1)
        missing = m
        
        for i, s in enumerate(s2):
            if s in d:
                if d[s] > 0:
                    missing -= 1
                d[s] -= 1
                
            if i >= m and s2[i-m] in d:
                d[s2[i-m]] += 1
                if d[s2[i-m]] > 0:
                    missing += 1
            if missing == 0:
                return True
                
        return False
        
