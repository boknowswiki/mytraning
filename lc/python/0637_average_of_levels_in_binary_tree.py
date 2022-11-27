
# binary tree and dfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.level = collections.defaultdict(list)
        self.dfs(root, 0)
        self.ret = []
        
        for i in range(len(self.level)):
            self.ret.append(sum(self.level[i])/len(self.level[i]))
            
        return self.ret
    
    def dfs(self, node, level):
        if not node:
            return
        
        self.dfs(node.left, level+1)
        self.level[level].append(node.val)
        self.dfs(node.right, level+1)
        
        return

# binary tree and bfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0]
        
        q = collections.deque([root])
        ret = []
        
        while q:
            cnt = len(q)
            total = 0
            for _ in range(cnt):
                cur = q.popleft()
                total += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                    
            ret.append(total/cnt)
            
        return ret
