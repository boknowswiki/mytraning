#!/usr/bin/python -t

# dfs

class Solution:
    """
    @param graph: a 2D array
    @return: all possible paths from node 0 to node N-1
    """
    def allPathsSourceTarget(self, graph):
        # Write your code here
        ret = []
        path = []
        path.append(0)
        self.dfs(graph, 0, path, ret)
        
        return ret
        
    def dfs(self, graph, index, path, ret):
        if index == len(graph)-1:
            ret.append(list(path))
            return
        
        for i in graph[index]:
            if i not in path:
                path.append(i)
                self.dfs(graph, i, path, ret)
                path.pop()
                
        return
    
    
        
        
if __name__ == '__main__':
    s= [[1,2],[3],[3],[]]
    ss = Solution()
    print "answer is %s" % ss.allPathsSourceTarget(s)

