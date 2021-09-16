#!/usr/bin/python -t

# dfs and multiple tree.

class MyTreeNode:
    """
    @param val: the node's val
    @return: a MyTreeNode object
    """
    def __init__(self, val):
        # write your code here
        self.val = val
        self.children = []
        self.parent = None
        self.is_deleted = False
        
    """
    @param root: the root treenode
    @return: get the traverse of the treenode
    """
    def traverse(self, root):
        # write your code here
        ret = []
        self.helper(ret, root)
        return ret

    def helper(self, ret, root):
        if root.is_deleted == False:
            ret.append(root.val)
        for child in root.children:
            self.helper(ret, child)

        return

    """
    @param root: the node where added
    @param value: the added node's value
    @return: add a node, return the node
    """
    def addNode(self, root, value):
        # write your code here
        newNode = MyTreeNode(value)
        newNode.parent = root
        root.children.append(newNode)

        return newNode

    """
    @param root: the deleted node
    @return: nothing
    """
    def deleteNode(self, root):
        # write your code here
        root.is_deleted = True
        return
