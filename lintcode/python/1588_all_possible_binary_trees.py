#!/usr/bin/python -t

# 考点：
# 
# 递归
# 记忆化搜索
# dfs
# 题解：递归的思想，现在这个树一共是N个节点的话，根节点算一个，左子树一共i个，那右子树一共就N-1-i个。然后迭代的时候每次左边+2个，右边-2个。把所有的结果加起来就好啦。

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param n: An integer
    @return: A list of root
    """
    def allPossibleFBT(self, n):
        # write your code here
        if n == 1:
            return [TreeNode(0)]
        if n % 2 == 0:
            return []
        ret = []
        left = 1
        right = n-left-1
        
        while right > 0:
            lefts = self.allPossibleFBT(left)
            rights = self.allPossibleFBT(right)
            for i in range(len(lefts)):
                for j in range(len(rights)):
                    root = TreeNode(0)
                    root.left = lefts[i]
                    root.right = rights[j]
                    ret.append(root)
                    
            left += 2
            right -= 2
            
        return ret
