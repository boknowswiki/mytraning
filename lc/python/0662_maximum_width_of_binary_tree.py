# bfs, binary tree

# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        # queue of elements [(node, col_index)]
        queue = deque()
        queue.append((root, 0))

        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]
            # iterate through the current level
            for _ in range(level_length):
                node, col_index = queue.popleft()
                # preparing for the next level
                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))

            # calculate the length of the current level,
            #   by comparing the first and last col_index.
            max_width = max(max_width, col_index - level_head_index + 1)

        return max_width
      
      
# dfs
# time O(n)
# space O(n)

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        # table contains the first col_index for each level
        first_col_index_table = {}
        max_width = 0

        def DFS(node, depth, col_index):
            nonlocal max_width
            if node is None:
                return
            # if the entry is empty, set the value
            if depth not in first_col_index_table:
                first_col_index_table[depth] = col_index

            max_width = max(max_width, col_index - first_col_index_table[depth] + 1)

            # Preorder DFS, with the priority on the left child
            DFS(node.left, depth+1, 2*col_index)
            DFS(node.right, depth+1, 2*col_index + 1)

        DFS(root, 0, 0)

        return max_width

# Time Limit Exceeded

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ret = 0

        def bfs(node):
            nonlocal ret
            q = collections.deque([node])
            ret = len(q)

            def validate(path):
                l = 0
                r = len(path)-1

                while l <= r:
                    if path[l] == None:
                        l += 1
                    else:
                        break

                while l <= r:
                    if path[r] == None:
                        r -= 1
                    else:
                        break

                if l <= r:
                    return r-l+1
                return 0

            while len(q) > 0:
                level = []
                has_value = False
                #print(f"q {q}")
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur:
                        has_value = True
                        level.append(cur.left)
                        level.append(cur.right)
                    else:
                        level.append(None)
                        level.append(None)

                #print(f"level {level}, has_value {has_value}")
                ret = max(ret, validate(level))
                if has_value:
                    q.extend(level)

        bfs(root)

        return ret
