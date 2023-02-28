# hash table, binary tree, tree and dfs
# time O(n)
# space O(n)


class Solution:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    ans = []
    count = collections.Counter()

    def encode(root: Optional[TreeNode]) -> str:
      if not root:
        return ''

      encoded = str(root.val) + '#' + \
          encode(root.left) + '#' + \
          encode(root.right)
      count[encoded] += 1
      if count[encoded] == 2:
        ans.append(root)
      return encoded

    encode(root)
    return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ret = []
        tree_map = dict()

        self.find(root, tree_map, ret)
        print(f"tree map {tree_map}")

        return ret

    def find(self, root, tree_map, ret):
        if not root:
            return

        self.find(root.left, tree_map, ret)
        self.find(root.right, tree_map, ret)

        data = []

        self.inorder(root, data)

        data_list = " ".join(data)
        if tree_map.get(data_list, 0) == 1:
            ret.append(root)

        tree_map[data_list] = tree_map.get(data_list, 0) + 1

        return

    def inorder(self, node, data):
        if not node:
            data.append("#")
            return
        
        data.append(str(node.val))
        self.inorder(node.left, data)
        self.inorder(node.right, data)

        return
