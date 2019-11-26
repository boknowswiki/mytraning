#!/usr/bin/python -t

# dfs
#输出到的矩阵的列数永远是奇数 -- 对于所有子树, 即原矩阵的子矩阵也是奇数. 因为是奇数时, 左右子树才能平分列数. 一棵高度为 height 的二叉树对应的矩阵是
# height * (2**height-1) 
#
#先 dfs 确定二叉树的高度, 然后定义字符串二维数组. 再次 dfs 把每一个节点的值填入二维数组即可. 第二次 dfs 的过程中需要记录以下信息:
#
#当前节点所在行, 列 -- 确定当前节点的值填入二维数组的哪个位置
#当前节点的子树的宽度 -- 确定该节点的左右子节点该填入的位置
#当前节点在 [row, col], 宽度是 width 时, 其左右子树的宽度均为 width / 2 - 1 (宽度永远是奇数), 左右子节点所在列与 col 的距离相同, 都是宽度的一半.
#
#总归, 两次dfs就可以解决这个问题.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: the binary tree in an m*n 2D string array
    """
    def printTree(self, root):
        # Write your code here
        height = self.get_height(root)
        
        col = 2**height-1
        
        ret = [[''] * col for _ in range(height)]
        
        self.dfs(root, 0, 0, col, ret)
        
        return ret
        
        
    def get_height(self, node):
        if not node:
            return 0
            
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
        
    def dfs(self, node, depth, start, end, ret):
        if not node:
            return
        
        mid = (start+end)/2
        ret[depth][mid] = str(node.val)
        self.dfs(node.left, depth + 1, start, mid-1, ret)
        self.dfs(node.right, depth + 1, mid+1, end, ret)
        
        return
    
    
