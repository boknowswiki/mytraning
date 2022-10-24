# binary tree and stack
# time O(n)
# space O(n)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root


# binary tree and dfs
# time O(nlogn)
# space O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(start, end):
            if start == end:
                return None
            
            root = TreeNode(preorder[start])
            mid = bisect.bisect_left(preorder, preorder[start], start+1, end)
            root.left = helper(start+1, mid)
            root.right = helper(mid, end)
            
            return root
        
        return helper(0, len(preorder))
