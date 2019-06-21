#!/usr/bin/python -t

#time O(S) space O(1)
#myself solution

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 0:
            return ""
        ret = strs[0]
        for i in range(1, n):
            for j in range(len(ret)):
                if j == len(strs[i]):
                    ret = ret[:j]
                    break
                if ret[j] != strs[i][j]:
                    ret = ret[:j]
                    break
        
        return ret
