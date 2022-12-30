# bfs

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        q = []
        mapping = collections.defaultdict(list)
        for i in range(len(graph)-1):
            mapping[i].extend(graph[i])

        print(f"mapping {mapping}")
        n = len(graph) - 1
        q.append([0])
        ret = []
        while q:
            cur = q.pop()
            #print(f"q {q}, cur {cur}")
            if cur[-1] not in mapping:
                ret.append(cur)
                continue
            for nxt in mapping[cur[-1]]:
                #print(f"nxt {nxt}")
                if nxt not in cur:
                    #cur.append(nxt)
                    #print(f"cur {cur}")
                    path = cur+[nxt]
                    #print(f"path {path}")
                    q.append(path)

        return ret
      
 # dfs

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        results = []

        def backtrack(curr_node, path):
            # if we reach the target, no need to explore further.
            if curr_node == target:
                results.append(list(path))
                return
            # explore the neighbor nodes one after another.
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()
        # kick of the backtracking, starting from the source node (0).
        path = [0]
        backtrack(0, path)

        return results
