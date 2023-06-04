# bfs
# time O(n^2)
# space O(n)

import collections

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        if n == 0:
            return 0

        ret = 0
        graph = collections.defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        v = set()

        def bfs(i):
            nonlocal v, graph
            q = collections.deque([i])

            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    for nei in graph[cur]:
                        if nei not in v:
                            v.add(nei)
                            q.append(nei)

            return

        for i in range(n):
            if i not in v:
                ret += 1
                v.add(i)
                if i not in graph:
                    continue
                bfs(i)

        return ret
      
      
# dfs

class Solution {
    public void dfs(int node, int[][] isConnected, boolean[] visit) {
        visit[node] = true;
        for (int i = 0; i < isConnected.length; i++) {
            if (isConnected[node][i] == 1 && !visit[i]) {
                dfs(i, isConnected, visit);
            }
        }
    }

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        int numberOfComponents = 0;
        boolean[] visit = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (!visit[i]) {
                numberOfComponents++;
                dfs(i, isConnected, visit);
            }
        }

        return numberOfComponents;
    }
}
