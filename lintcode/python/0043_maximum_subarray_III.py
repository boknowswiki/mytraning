#!/usr/bin/python -t

# dp solution, time O(nk) space O(nk)

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        # state: dp_l[i][j], max sum must include i point in group j
        #        dp_g[i][j], max sum may not include i point in group j
        # function: dp_l[i][j] = max(dp_l[i-1][j]+nums[i], dp_g[i-1][j-1]+nums[i])
        #           dp_g[i][j] = max(dp_g[i-1][j], dp_l[i][j])
        # init: dp_l[i][0] = dp_g[i][0] = 0
        # result: dp_g[k][n]
        
        n = len(nums)
        if n == 0 or k == 0:
            return 0
            
        dp_l = [[0] * (k+1) for i in range(n+1)]
        dp_g = [[0] * (k+1) for i in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, k+1):
                #千万注意 i ＝＝ j的时候 只能一种划分！
                if i == j:
                    dp_l[i][j] = dp_l[i-1][j-1] + nums[i-1]
                    dp_g[i][j] = dp_l[i][j]
                    print i, j
                    print dp_l[i][j], dp_l[i-1][j-1]
                else:
                    dp_l[i][j] = max(dp_l[i-1][j], dp_g[i-1][j-1]) + nums[i-1]
                    dp_g[i][j] = max(dp_g[i-1][j], dp_l[i][j])
        print dp_l
        print dp_g
                    
        return dp_g[n][k]

if __name__ == '__main__':
    s = [1,2,3]
    k = 1
    s = [-1,4,-2,3,-2,3]
    k = 2
    s = [-1,0,1]
    k = 3
    ss = Solution()
    print "answer is %s" % ss.maxSubArray(s, k)
# dp solution

        MIN = - 2 ** 32
        n = len(nums)
        
        array = [0]
        for num in nums:
            array.append(num)
        
        # include the last num
        ans1 = [[MIN for i in range(k + 1)] for j in range(n + 1)]
        
        # do not include the last num
        ans2 = [[MIN for i in range(k + 1)] for j in range(n + 1)]
        
        for i in range(n + 1):
            ans1[i][0] = 0
            ans2[i][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                   ans1[i][j] = max(ans1[i - 1][j] + array[i], ans1[i - 1][j -  1] + array[i], ans2[i - 1][j -  1] + array[i])
                   ans2[i][j] = max(ans1[i - 1][j], ans2[i - 1][j])
            
        return max(ans1[n][k], ans2[n][k])

