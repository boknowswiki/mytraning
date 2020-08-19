
import bisect

class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        envelopes = sorted(envelopes, key = lambda x:(x[0], -x[1]))
        n = len(envelopes)
        dp = [0] * n
        ret = 0
        
        for e in envelopes:
            index = bisect.bisect_left(dp,e[1], 0, ret)
            dp[index] = e[1]
            if index == ret:
                ret += 1
                
        return ret
