#!/usr/bin/python

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class Answer:
    def getMaxPath(self, root):
        if root == None:
            return 0

        ret = self.dfs(root)

        return ret

    def dfs(self, root):
        if len(root.neighbors) == 0:
            return 1

        ret = 0
        sub_ret = 0
        print root.val
        for nei in root.neighbors:
            print nei.val
            sub_ret += self.dfs(nei)
            ret = max(ret, sub_ret)
    
        return ret

if __name__ == '__main__':
    node_a = Node('a')
    node_b = Node('b')
    node_c = Node('c')
    node_d = Node('d')
    node_e = Node('e')
    node_a.neighbors.append(node_b)
    node_a.neighbors.append(node_c)
    #node_a.neighbors.append(node_d)
    #node_b.neighbors.append(node_d)
    #node_c.neighbors.append(node_d)
    #node_c.neighbors.append(node_e)
    #node_d.neighbors.append(node_e)
 
    ss = Answer()
    print "answer is %s" % ss.getMaxPath(node_a)
