#!/usr/bin/python -t

# bfs

import collections

class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        # Write your code here
        graph = self.build_graph(length, connections)
        q = collections.deque([1])
        dist = {
            i: float('inf') for i in range(1, length+1)
        }
        dist[1] = 0

        while q:
            p = q.popleft()
            for next_p in graph[p]:
                if dist[next_p] > dist[p]:
                    dist[next_p] = dist[p]
                    q.append(next_p)
            for next_p in range(p+1, min(p+7, length+1)):
                if dist[next_p] > dist[p]+1:
                    dist[next_p] = dist[p]+1
                    q.append(next_p)

        return dist[length]


    def build_graph(self, length, connections):
        graph = {
            i: set() for i in range(1, length+1)
        }
                    
        for k, v in connections:
            graph[k].add(v)

        return graph


# BFS+BFS解法。外层 BFS 做最短路径，内层 BFS 找连通块。


class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        from collections import deque
        
        graph = self.build_graph(length, connections)
        
        queue = deque([1])
        distance = {1: 0}
        while queue:
            node = queue.popleft()
            for neighbor in range(node + 1, min(node + 7, length + 1)):
                connected_nodes = self.get_unvisited_nodes(graph, distance, neighbor)
                for connected_node in connected_nodes:
                    distance[connected_node] = distance[node] + 1
                    queue.append(connected_node)
        return distance[length]

    def build_graph(self, length, connections):
        graph = {
            i: set()
            for i in range(1, length + 1)
        }
        for a, b in connections:
            graph[a].add(b)
        return graph
        
    def get_unvisited_nodes(self, graph, distance, node):
        from collections import deque
        queue = deque([node])
        unvisited_nodes = set()
        while queue:
            node = queue.popleft()
            if node in distance:
                continue
            unvisited_nodes.add(node)
            for neighbor in graph[node]:
                if neighbor not in distance:
                    queue.append(neighbor)
                    unvisited_nodes.add(neighbor)
        return unvisited_nodes
