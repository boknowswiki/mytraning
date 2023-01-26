# bfs

import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        graph = collections.defaultdict(list)
        for i in range(len(flights)):
            graph[flights[i][0]].append((flights[i][1], flights[i][2]))

        #print(f"graph {graph}")
        q = [(src, 0)]

        ret = [sys.maxsize] * n
        ret[src] = 0

        while q and k >= 0:
            nxt = []
            for _ in range(len(q)):
                #print(f"q {q}")
                cur, price = q.pop()
                #print(f"cur {cur}, price {price}")

                if cur in graph:
                    for d, p in graph[cur]:
                        #print(f"d {d}, p {p}")
                        if p+price >= ret[d]:
                            continue
                        ret[d] = p+price
                        nxt.append((d, price+p))

            q = nxt
            k -= 1

        return ret[dst] if ret[dst] != sys.maxsize else -1
      
 # bfs
# Time Limit Exceeded

import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        graph = collections.defaultdict(list)
        for i in range(len(flights)):
            graph[flights[i][0]].append((flights[i][1], flights[i][2]))

        #print(f"graph {graph}")

        q = [(src, 0)]

        ret = -1

        while q and k+1 >= 0:
            nxt = []
            for _ in range(len(q)):
                #print(f"q {q}")
                cur, price = q.pop()
                #print(f"cur {cur}, price {price}")
                if cur == dst:
                    if ret == -1 or ret > price:
                        ret = price

                if cur in graph:
                    for d, p in graph[cur]:
                        #print(f"d {d}, p {p}")
                        nxt.append((d, price+p))

            q = nxt
            k -= 1

        return ret
      
      
      
      
