# bfs
# time O(n)
# space O(n)

import collections

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = dict()
        for i, edge in enumerate(edges):
            graph[i] = edge

        def get_list(node):
            l = [sys.maxsize] * len(edges)
            v = set()
            q = collections.deque([node])
            l[node] = 0
            v.add(node)
            while q:
                cur = q.popleft()
                nei = graph[cur]
                if nei != -1 and nei not in v:
                    v.add(nei)
                    l[nei] = l[cur]+1
                    q.append(nei)

            return l

        
        l1_dist = get_list(node1)
        l2_dist = get_list(node2)

        #print(f"l1 {l1_dist}, l2 {l2_dist}")
        ret = -1
        cur_min = sys.maxsize
        for i in range(len(edges)):
            if cur_min > max(l1_dist[i], l2_dist[i]):
                ret = i
                cur_min = max(l1_dist[i], l2_dist[i])

        return ret
