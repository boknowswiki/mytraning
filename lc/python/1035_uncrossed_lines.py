# dp

# time O(n1*n2)
# space O(n2)

class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        
        dp = [0] * (n2 + 1)
        dpPrev = [0] * (n2 + 1)

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = 1 + dpPrev[j - 1]
                else:
                    dp[j] = max(dp[j - 1], dpPrev[j])
            dpPrev = dp[:]

        return dp[n2]
      
# time O(m*n)
# space O(m*n)

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] is the max number of lines at ith in nums1, jth in nums2.
        # dp[i][j] = 1 + dp[i-1][j-1] if nums1[i-1] == nums2[j-1] else dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # init dp[i][j] = 0, i, j in range of 1 to len(nums1), 1 to len(nums2)
        # return dp[m][n]
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]
