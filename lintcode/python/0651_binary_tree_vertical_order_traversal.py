#!/usr/bin/python -t

# hash table

# 对于一棵树，我们设其根节点的位置为0。
# 对于任一非叶子节点，若其位置为x，设其左儿子的位置为x-1，右儿子位置为x+1。
# 按照以上规则bfs遍历整棵树统计所有节点的位置，然后按位置从小到大输出所有节点。

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import collections

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        if not root:
            return []
            
        #q = collections.deque()
        ret = collections.defaultdict(list)
        q = collections.deque([(0, root)])
        print q
        
        while len(q) != 0:
            index, node = q.popleft()
            ret[index].append(node.val)
            if node.left:
                q.append((index-1, node.left))
            if node.right:
                q.append((index+1, node.right))
                
        return [ret[i] for i in sorted(ret)]
        
