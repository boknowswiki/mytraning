#!/usr/bin/python -t

# two pointers
#维护一个 当前子串长度 - 最大count字符长度 == k 的window，不断的移动，如果 大于k了，left指针移动一格，同时更新对应的字符数目，否则计算 right - left + 1和之前max值的大小

#时间复杂度0(n)
#空间复杂度O(26)因为需要一个数组作为map使用



class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        # write your code here
        n = len(s)
        if n == 0:
            return 0
            
        max_cnt = 0
        d = {}
        ret = 0
        left = 0
        
        for right in range(n):
            d[s[right]] = d.get(s[right], 0) + 1
            max_cnt = max(max_cnt, d[s[right]])
            diff = right-left + 1 - max_cnt
            if diff > k:
                d[s[left]] -= 1
                left += 1
            else:
                ret = max(ret, right-left+1)
                
        return ret
        
        
