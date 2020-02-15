#!/usr/bin/python

# no loop case

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class Answer:
    def getMaxPath(self, root):
        if root == None:
            return 0

        # all the posisible paths from root to the end
        paths = []
        # every dfs path from root to the end
        path = root.val
        ret = self.dfs(root, path, paths)
        print paths

        return ret

    def dfs(self, node, path, paths):
        if len(node.neighbors) == 0:
            paths.append(path)
            return 0

        ret = 0
        sub_ret = 0
        for nei in node.neighbors:
            sub_ret = self.dfs(nei, path + "->" + nei.val, paths)
            ret = max(ret, sub_ret)
    
        return ret+1

if __name__ == '__main__':
    node_a = Node('a')
    node_b = Node('b')
    node_c = Node('c')
    node_d = Node('d')
    node_e = Node('e')
    node_a.neighbors.append(node_b)
    node_a.neighbors.append(node_c)
    node_a.neighbors.append(node_d)
    node_b.neighbors.append(node_d)
    node_c.neighbors.append(node_d)
    node_c.neighbors.append(node_e)
    node_d.neighbors.append(node_e)
 
    ss = Answer()
    print "answer is %s" % ss.getMaxPath(node_a)

