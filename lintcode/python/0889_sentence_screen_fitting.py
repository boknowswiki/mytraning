#!/usr/bin/python -t

# dp solution, time O(n^2) space O(n)

class Solution:
    """
    @param sentence: a list of string
    @param rows: an integer
    @param cols: an integer
    @return: return an integer, denote times the given sentence can be fitted on the screen
    """
    def wordsTyping(self, sentence, rows, cols):
        # Write your code here
        #dp[i] : row start from sentence[i], can put how many word from i in sentence, inclusive
        n = len(sentence)
        dp = [0] * n
        for i in range(n):
            cnt = 0
            cur_size = 0
            while (cur_size + len(sentence[(i+cnt)%n]) <= cols):
                cur_size += len(sentence[(i+cnt)%n])+1
                cnt += 1
            #if we have a word that can't fit into a row, this won't work 
            if cnt == 0:
                return 0
            dp[i] = cnt
        total = 0
        idx = 0
        for i in range(rows):
            total += dp[idx]
            idx = (idx+dp[idx]) % n
        return total/n

