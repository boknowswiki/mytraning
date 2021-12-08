#!/usr/bin/python -t

# string

# 我们每次考虑生成从当前的I到上一个I所需要放置的字母。由于这两个I之间全部是D，或者没有，所以一定是降序排列的。由于要求的是最小的字典序，所以我们直接从最小的数开始倒着放置即可。

class Solution:
    """
    @param str: the pattern
    @return: the minimum number
    """
    def formMinimumNumber(self, str):
        # Write your code here.
        n = len(str)
        ret = ["0"]*(n+1)
        cnt = 1

        for i in range(n+1):
            if i == n or str[i] == 'I':
                for j in range(i-1, -2, -1):
                    ret[j+1] = chr(ord("0")+cnt)
                    cnt += 1
                    if j >= 0 and str[j] == 'I':
                        break
        return ''.join(ret)
