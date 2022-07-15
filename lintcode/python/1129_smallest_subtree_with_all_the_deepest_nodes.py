#!/usr/bin/python3 -t

# binary tree
# divid and conquer way
# time O(n)
# space O(n)

class Solution:
    """
    @param root: a binary tree.
    @return: return the minimun subtree contains all the key nodes.
    """
    def subtree_with_all_key_nodes(self, root: TreeNode) -> TreeNode:
        # write your code here.
        node, _ = self.helper(root, 0)

        return node

    def helper(self, node, dep):
        if not node:
            return node, dep

        l_node, l_dep = self.helper(node.left, dep+1)
        r_node, r_dep = self.helper(node.right, dep+1)

        if l_dep == r_dep:
            return node, l_dep

        if l_dep > r_dep:
            return l_node, l_dep

        return r_node, r_dep
