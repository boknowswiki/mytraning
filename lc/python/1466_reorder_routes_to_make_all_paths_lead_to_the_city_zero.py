# bfs
# time O(n)
# space O(n)

import collections

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        direct_to = collections.defaultdict(list)
        direct_from = collections.defaultdict(list)

        for con in connections:
            direct_from[con[1]].append(con[0])
            direct_to[con[0]].append(con[1])

        #print(f"to {direct_to}, from {direct_from}")
        q = collections.deque([0])
        v = set()
        v.add(0)
        ret = 0

        while q:
            cur = q.popleft()

            for nei in direct_from[cur]:
                if nei not in v:
                    v.add(nei)
                    q.append(nei)
                    
            for nei in direct_to[cur]:
                if nei not in v:
                    #print(f"cur {cur}, nei {nei}")
                    v.add(nei)
                    q.append(nei)
                    ret += 1


        return ret

# Time Limit Exceeded
import collections

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        no_change = collections.defaultdict(list)
        change = collections.defaultdict(list)

        for con in connections:
            no_change[con[1]].append(con[0])
            change[con[0]].append(con[1])

        #print(f"no_chnage {no_change} change {change}")
        q = collections.deque([0])
        v = set()
        v.add(0)
        ret = 0

        while q:
            cur = q.popleft()

            for nei in change[cur]:
                if nei not in v:
                    #print(f"cur {cur}, nei {nei}")
                    v.add(nei)
                    q.append(nei)
                    ret += 1
            
            for key, val in no_change.items():
                #print(f"cur {cur}, key {key}, val {val}")
                if cur == key:
                    for a in val:
                        if a not in v:
                            v.add(a)
                            q.append(a)

        return ret
