#!/usr/bin/python -t

# monotonic stack
# time O(n) space O(n)

# 使用九章算法强化班中讲过的单调栈。另外一种比较简洁的写法。
# 
# 考点：
# 
# 数据结构设计
# 树的调整
# 单调栈
# 题解：
# 利用数组实现基本数据结构的调整，当前遍历到的数字比stk中的最后一个大时，将stk中的最后一个数字转变为当前节点的左子树，循环调整至stk为空或者stk中的最后节点值大于新节点的值。如果stk不为空，说明stk中的最后一个节点值大于新节点值，则将新节点设为stk中的最后一个节点的右子树，将新节点存入stk。

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        # write your code here
        stack = []
        
        for num in A:
            node = TreeNode(num)
            
            while len(stack) != 0 and stack[-1].val < num:
                node.left = stack.pop()
                
            if len(stack) != 0:
                stack[-1].right = node
                
            stack.append(node)
            
        return stack[0]
