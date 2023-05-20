
# bfs
# time O(n)
# space O(n)


import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)

        for i, e in enumerate(equations):
            graph[e[0]].append([e[1], values[i]])
            graph[e[1]].append([e[0], 1/values[i]])

        def helper(a, b):
            nonlocal graph
            if a not in graph or b not in graph:
                return -1.0

            v = set()
            q = collections.deque([(a, 1.0)])
            v.add(a)

            while q:
                cur = q.popleft()
                if cur[0] == b:
                    return cur[1]

                if cur[0] in graph:
                    for nei in graph[cur[0]]:
                        if nei[0] not in v:
                            v.add(nei[0])
                            q.append((nei[0], nei[1]*cur[1]))

            return -1.0

        ret = []

        for a, b in queries:
            val = helper(a, b)
            ret.append(float(val))

        return ret

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        form = dict()
        for i in range(len(equations)):
            a, b = equations[i]
            #print(f"form {form}, {a}, {b}")
            if a not in form:
                form[a] = []
            if b not in form:
                form[b] = []
            form[a].append((b, values[i]))
            form[b].append((a, 1/values[i]))
            
        #print(f"form {form}")
        ret = []
        
        for query in queries:
            a, b = query
            val = self.helper(a, b, form)
            ret.append(float(val))
            
        return ret
    
    def helper(self, a, b, form):
        #print(f"helper {a}, {b}")
        if a not in form or b not in form:
            return -1.00000
        q = collections.deque([(a, 1.0)])
        v = set()
        v.add(a)
        while q:
            cur, val = q.popleft()
            if cur == b:
                return val
            if cur in form:
                for f in form[cur]:
                    if f[0] not in v:
                        #print(f"f is {f}")
                        v.add(f[0])
                        q.append((f[0], f[1]*val))
                    
        return -1.00000

    
    # dfs
    
    
    class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(defaultdict)

        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret = -1.0
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product * value, visited)
                    if ret != -1.0:
                        break
            visited.remove(curr_node)
            return ret

        # Step 1). build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Step 2). Evaluate each query via backtracking (DFS)
        #  by verifying if there exists a path from dividend to divisor
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # case 1): either node does not exist
                ret = -1.0
            elif dividend == divisor:
                # case 2): origin and destination are the same node
                ret = 1.0
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            results.append(ret)

        return results
