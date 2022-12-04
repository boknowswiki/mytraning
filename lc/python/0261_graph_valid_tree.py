# dfs
# time O(n)
# space O(n)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        v = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        self.dfs(graph, 0, v)
        
        return len(v) == n
    
    def dfs(self, graph, node, v):
        if node in v:
            return
        
        v.add(node)
        for nei in graph[node]:
            self.dfs(graph, nei, v)
            
        return
