# binary tree and bfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        
        ret = []
        
        q = collections.deque([root])
        
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                ret.append(str(node.val))
            else:
                ret.append("#")
                
        return " ".join(ret)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return []
        data_list = data.split()
        node_list = [TreeNode(val=int(x)) if x != "#" else None for x in data_list]
        
        root = node_list[0]
        index = 0
        child_index = 0
        
        while child_index + 2 < len(node_list):
            node = node_list[index]
            left = node_list[child_index+1]
            right = node_list[child_index+2]
            if node:
                node.left = left
                node.right = right
                child_index +=2
            index += 1
            
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

# binary tree
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        vals = []

        def preOrder(node):
            if node:
                vals.append(str(node.val))
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(vals)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        vals = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))
    
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
