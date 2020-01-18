#!/usr/bin/python -t

# two pointers and pre_sum


class Solution:
    """
    @param k: The number of words in the article
    @param lim: TThe minimum number of words a phrase should contain 
    @param str: The article
    @return: Return the length of shortest phrase
    """
    def getLength(self, k, lim, str):
        # Write your code here
        n = len(str)
        ret = 1e9
        
        len_list = [0] * n
        
        for i in range(n):
            len_list[i] = len(str[i])
                
        left = 0
        val = 0
        
        for right in range(n):
            val += len_list[right]
            
            while right-left >= k and val - len_list[left] >= lim:
                val -= len_list[left]
                left += 1
                
            if right-left+1>= k and val >= lim:
                ret = min(ret, val)
            
        return ret
        
