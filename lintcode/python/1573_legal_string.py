#!/usr/bin/python -t

# greedy and string

# 我们贪心的考虑这个问题，由于字典序需要最小，所以我们尽量让'_'的位置靠后，也就是从前往后考虑，当当前位置字母的前一个同类字母离它距离小于k时我们才在当前字母前面插入'_'.
# 具体做法如下我们将原字符串扫一遍，维护一个sum[]数组当前位置之前的'_'的总数，维护一个pre[]数组，pre[i]表示当前位置之前的最靠右的字母'i'的位置，这样每扫到一个位置k,我们就可以利用这两个数组O(1)得到这个位置之前需要插入多少个'_'了。
# 总复杂度O(|S|)

class Solution:
    """
    @param k: The necessary distance of same kind of letters
    @param S: The original string
    @return: Return the number of '_' inserted before each position of the original string
    """
    def getAns(self, k, S):
        # Write your code here.
        pre = [-1] * 26
        n = len(S)
        sm = [0] * 500100
        ans = []
        for i in range(1, n + 1):
            c = ord(S[i - 1]) - ord('A')
            if pre[c] == -1 or sm[i - 1] - sm[pre[c]] - pre[c] + i >= k:
                sm[i] = sm[i - 1]
                ans.append(0)
            else:
                sm[i] = sm[i - 1] + k - (sm[i - 1] - sm[pre[c]] + i - pre[c])
                ans.append(k - (sm[i - 1] - sm[pre[c]] + i - pre[c]))
            pre[c] = i
        return ans
