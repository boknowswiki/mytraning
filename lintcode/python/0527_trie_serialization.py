#!/usr/bin/python -t

"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
"""


class Solution:

    '''
    @param root: An object of TrieNode, denote the root of the trie.
    This method will be invoked first, you should design your own algorithm 
    to serialize a trie which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # Write your code here
        if not root:
            return ""
            
        data = ""
        for k, v in root.children.items():
            data += k + self.serialize(v)
            
        #print data
        return "<%s>" % data

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # Write your code here
        if not data or len(data) == 0:
            return None
            
        root = TrieNode()
        cur = root
        path = []
        
        for c in data:
            if c == "<":
                path.append(cur)
            elif c == ">":
                path.pop()
            else:
                cur = TrieNode()
                if len(path) == 0:
                    print cur, path
                path[-1].children[c] = cur
                
        return root
        

