#!/usr/bin/python -t

# two pointers
# 按字符分割：
# 预处理每个位置 i，左边第一个和自己一样字符的位置 left，
# 右边第一个和自己一样字符的位置 right。
# 该位置 i 贡献的答案就是 (i - left) * (right - i)。
# 对每个位置进行统计。


import string

class Solution:
    """
    @param S: a string
    @return: the sum of UNIQ(substring) over all non-empty substrings of S
    """
    def uniqueLetterString(self, S):
        # Write your code here
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(S):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        return res % (10**9 + 7)
        
