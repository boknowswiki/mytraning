# bfs

import collections

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        con_len = len(connections)
        if con_len < n-1:
            return -1

        graph = collections.defaultdict(list)

        for con in connections:
            graph[con[0]].append(con[1])
            graph[con[1]].append(con[0])

        ret = 0
        v = set()
        for i in range(n):
            if i not in v:
                ret += 1
                self.bfs(i, graph, v)

        return ret - 1

    def bfs(self, node, graph, v):
        q = collections.deque([node])
        v.add(node)

        while q:
            cur = q.popleft()
            if cur not in graph:
                continue
            
            for nei in graph[cur]:
                if nei not in v:
                    v.add(nei)
                    q.append(nei)

        return
      
      
class UnionFind {
    int[] parent;
    int[] rank;

    public UnionFind(int size) {
        parent = new int[size];
        for (int i = 0; i < size; i++)
            parent[i] = i;
        rank = new int[size];
    }

    public int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    public void union_set(int x, int y) {
        int xset = find(x), yset = find(y);
        if (xset == yset) {
            return;
        } else if (rank[xset] < rank[yset]) {
            parent[xset] = yset;
        } else if (rank[xset] > rank[yset]) {
            parent[yset] = xset;
        } else {
            parent[yset] = xset;
            rank[xset]++;
        }
    }
}

class Solution {
    public int makeConnected(int n, int[][] connections) {
        if(connections.length < n-1) {
            return -1;
        }

       UnionFind dsu = new UnionFind(n);
        int numberOfConnectedComponents = n;
        for (int[] connection : connections) {
            if (dsu.find(connection[0]) != dsu.find(connection[1])) {
                numberOfConnectedComponents--;
                dsu.union_set(connection[0], connection[1]);
            }
        }

        return numberOfConnectedComponents - 1;
    }
}
