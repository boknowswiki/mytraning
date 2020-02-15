#!/usr/bin/python

# with loop case

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
        # visited hash set to remember all visited node to prevent loop
        visited = set()
        visited.add(root)
        ret, has_loop = self.dfs(root, path, paths, visited)
        print paths, has_loop

        return ret

    def dfs(self, node, path, paths, visited):
        if len(node.neighbors) == 0:
            paths.append(path)
            return 0, False

        ret = 0
        sub_ret = 0
        has_loop = False
        for nei in node.neighbors:
            if nei in visited:
                paths.append(path)
                return 0, True
            visited.add(nei)
            sub_ret, has_loop = self.dfs(nei, path + "->" + nei.val, paths, visited)
            visited.remove(nei)
            ret = max(ret, sub_ret)
    
        return ret+1, has_loop

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
    # add this neighbor to create a loop
    node_e.neighbors.append(node_a)
 
    ss = Answer()
    print "answer is %s" % ss.getMaxPath(node_a)

