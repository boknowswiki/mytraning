#!/usr/bin/python -t

# dp solution, time O(n) space O(n)

#参考ainkin0617
#这是很有意思的一个题。刚拿到这题的时候，完全不知道从那下手，因为对于BST是否Unique，很难判断。最后引入了一个条件以后，立即就清晰了，即
#当数组为 1，2，3，4，.. i，.. n时，基于以下原则的BST建树具有唯一性：
#以i为根节点的树，其左子树由[0, i-1]构成， 其右子树由[i+1, n]构成。
#
#定义f(n)为unique BST的数量，以n = 3为例：
#
#构造的BST的根节点可以取{1, 2, 3}中的任一数字。
#
#如以1为节点，则left subtree只能有0个节点，而right subtree有2, 3两个节点。所以left/right subtree一共的combination数量为：f(0) * f(2) = 2
#
#以2为节点，则left subtree只能为1，right subtree只能为2：f(1) * f(1) = 1
#
#以3为节点，则left subtree有1, 2两个节点，right subtree有0个节点：f(2)*f(0) = 2
#
#总结规律：
#f(0) = 1
#f(n) = f(0)*f(n-1) + f(1)*f(n-2) + ... + f(n-2)*f(1) + f(n-1)*f(0)

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        # write your code here
        # state: dp[i] is the unique BST at point i
        # function: dp[i] = sum(dp[0..k]*dp[k+1...i])
        # init: dp[0] = 0, dp[1] = 1, dp[2] = 2
        # result dp[n]
        # the reason for n+2 is for case n = 0, and dp[1] doesn't exist, we extend the array by 1 to cover this case
        dp = [0] * (n+2)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
                
        return dp[n]

