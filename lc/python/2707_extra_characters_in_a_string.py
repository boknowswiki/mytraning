# dp bottom up

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dp[i] is the min extra characters at ith index
        # dp[i] = min(dp[i], dp[end+1]) for i:end+1 in dictionary
        # dp[i] = n-i
        # return dp[0]
        n, d_set = len(s), set(dictionary)
        dp = [0] * (n+1)

        for start in range(n-1, -1, -1):
            dp[start] = dp[start+1]+1
            for end in range(start, n):
                cur = s[start:end+1]
                if cur in d_set:
                    dp[start] = min(dp[start], dp[end+1])

        return dp[0]
      

# dfs with memo top down

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, dictionary_set = len(s), set(dictionary)
        @cache
        def dp(start):
            if start == n:
                return 0
            # To count this character as a left over character 
            # move to index 'start + 1'
            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    ans = min(ans, dp(end + 1))
            return ans
            
        return dp(0)

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # dfs[i] is the min extra need starting at ith index
        # dfs[i] = min(dfs[i], dfs(i+1))
        # memo[i] = None for i in range(len(s))
        # return dp[0]
        n, d_set = len(s), set(dictionary)
        memo = [None] * n
        def dfs(start):
            if start == n:
                return 0
            if memo[start]:
                return memo[start]

            ret = dfs(start+1) + 1
            for i in range(start, n):
                cur = s[start:i+1]
                if cur in d_set:
                    ret = min(ret, dfs(i+1))

            memo[start] = ret

            return memo[start]

        return dfs(0)
