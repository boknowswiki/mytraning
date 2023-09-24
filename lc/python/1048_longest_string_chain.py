# dfs and memo
# time O(l^2*n), l is the max length in words, n is the number of words
# space O(n)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        memo = dict()
        ret = 0

        def dfs(w):
            nonlocal memo, word_set
            if w in memo:
                return memo[w]
            
            max_l = 1

            for i in range(len(w)):
                new_w = w[:i] + w[i+1:]
                if new_w in word_set:
                    cur_l = 1 + dfs(new_w)
                    max_l = max(max_l, cur_l)

            memo[w] = max_l

            return max_l 

        for word in words:
            ret = max(ret, dfs(word))

        return ret
