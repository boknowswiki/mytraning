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
        #visited = set()
        node_mem = {root:(-1, False)}
        #visited.add(root)
        #ret, has_loop = self.dfs(root, path, paths, visited, node_mem)
        ret, has_loop = self.dfs(root, path, paths, node_mem)
        print paths, has_loop

        return ret

    #def dfs(self, node, path, paths, visited, node_mem):
    def dfs(self, node, path, paths, node_mem):
        if len(node.neighbors) == 0:
            paths.append(path)
            return 0, False

        if node in node_mem and node_mem[node][0] != -1:
            return node_mem[node]

        ret = 0
        sub_ret = 0
        has_loop = False
        for nei in node.neighbors:
            if nei in node_mem:
                paths.append(path)
                return 0, True
            #visited.add(nei)
            sub_ret, has_loop = self.dfs(nei, path + "->" + nei.val, paths, node_mem)
            #visited.remove(nei)
            ret = max(ret, sub_ret)
            node_mem[nei] = (ret, has_loop)
    
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

