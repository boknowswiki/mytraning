#!/usr/bin/python -t

# BFS

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        
        return topo_order == org
        
        
    def build_graph(self, seqs):
        g = {}
        
        for seq in seqs:
            for node in seq:
                if node not in g:
                    g[node] = set()
                    
        for seq in seqs:
            for i in range(1, len(seq)):
                g[seq[i-1]].add(seq[i])
                
        return g
        
    def get_depth(self, g):
        dep = {node:0 for node in g}
        
        for node in g:
            for nei in g[node]:
                dep[nei] += 1
                
        return dep
        
    def topological_sort(self, g):
        dep = self.get_depth(g)
        
        q = []
        
        for node in g:
            if dep[node] == 0:
                q.append(node)
                
        topo_order = []
        
        while q:
            if len(q) > 1:
                return None
                
            node = q.pop()
            topo_order.append(node)
            
            for nei in g[node]:
                dep[nei] -= 1
                if dep[nei] == 0:
                    q.append(nei)
                    
        if len(topo_order) == len(g):
            return topo_order
        
        return None
                

