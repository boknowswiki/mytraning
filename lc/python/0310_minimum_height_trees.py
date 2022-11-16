# bfs and topological sort
# time O(n)
# space O(n)

# reference: https://leetcode.com/problems/minimum-height-trees/solution/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        conns = [set() for i in range(n)]
        
        for x, y in edges:
            conns[x].add(y)
            conns[y].add(x)
            
        q = []
        
        for i in range(n):
            if len(conns[i]) == 1:
                q.append(i)
                
        remain_nodes = n
        
        while remain_nodes > 2:
            remain_nodes -= len(q)
            new_q = []
            while q:
                cur = q.pop()
                conn = conns[cur].pop()
                conns[conn].remove(cur)
                if len(conns[conn]) == 1:
                    new_q.append(conn)
                    
            q = new_q
            
        return q
