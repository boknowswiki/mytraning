# graph, dfs


import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for t in tickets:
            graph[t[0]].append(t[1])

        #print(f"before sort {graph}")
        for _, v in graph.items():
            v.sort(reverse=True)

        #print(f"sorted {graph}")

        ret = []

        def dfs(cur):
            nonlocal ret, graph
            #print(f"cur {cur}")
            dest_list = graph[cur]
            while dest_list:
                dest = dest_list.pop()
                #print(f"poped {dest}")
                dfs(dest)

            ret.append(cur)
            #print(f"ret is {ret}")

        dfs("JFK")

        return ret[::-1]
