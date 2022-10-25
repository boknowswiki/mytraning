# binary tree and bfs
# time O(n)
# space O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        q = collections.deque([root])
        ret = []
        
        while q:
            node = q.popleft()
            if node:
                ret.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ret.append("#")
                
        return " ".join(ret)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data_list = data.split()
        node_list = [TreeNode(int(x)) if x != "#" else None for x in data_list]
        root = node_list[0]
        index = 0
        child = 0
        
        while child + 2 < len(node_list):
            left = node_list[child+1]
            right = node_list[child+2]
            
            node = node_list[index]
            if node:
                node.left = left
                node.right = right
                child += 2
                
            index += 1
            
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
