# bfs

import collections

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)

        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)

        q = collections.deque([(headID, 0)])

        ret = 0

        while q:
            for _ in range(len(q)):
                p, t = q.popleft()
                #print(f"p {p}, t {t}")
                for child in graph[p]:
                    q.append((child, t+informTime[p]))
                ret = max(ret, t)

        return ret
      
class Solution {
    int maxTime = Integer.MIN_VALUE;

    void DFS(ArrayList<ArrayList<Integer>> adjList, int[] informTime, int curr, int time) {
        // Maximum time for an employee to get the news.
        maxTime = Math.max(maxTime, time);

        for (int adjacent : adjList.get(curr)) {
            // Visit the subordinate employee who gets the news after informTime[curr] unit time.
            DFS(adjList, informTime, adjacent, time + informTime[curr]);
        }
    }

    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<ArrayList<Integer>>(n);

        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<Integer>());
        }

        // Making an adjacent list, each index stores the Ids of subordinate employees.
        for (int i = 0; i < n; i++) {
            if (manager[i] != -1) {
                adjList.get(manager[i]).add(i);
            }
        }

        DFS(adjList, informTime, headID, 0);
        return maxTime;
    }
}
