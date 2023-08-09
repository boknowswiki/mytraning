#!/usr/bin/python -t

# array, string
# time O(mn)
# space O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        if n == 1:
            return strs[0]

        ret = ""
        min_len = min([len(s) for s in strs])
        break_flag = False

        for i in range(min_len):
            for j in range(1, n):
                if strs[j][i] != strs[j-1][i]:
                    break_flag = True
                    break
                if j == n-1:
                    ret += strs[j][i]

            if break_flag:
                break
        return ret

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
