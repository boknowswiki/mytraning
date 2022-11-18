
# bfs
# time O(n)
# space O(n)

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
