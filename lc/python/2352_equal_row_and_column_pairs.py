# hash table, matrix

# trie
# time O(n^2)
# space O(n^2)

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, array):
        my_trie = self.trie
        for a in array:
            if a not in my_trie.children:
                my_trie.children[a] = TrieNode()
            my_trie = my_trie.children[a] 
        my_trie.count += 1

    def search(self, array):
        my_trie = self.trie
        for a in array:
            if a in my_trie.children:
                my_trie = my_trie.children[a]
            else:
                return 0
        return my_trie.count

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        my_trie = Trie()
        count = 0
        n = len(grid)
        
        for row in grid:
            my_trie.insert(row)
        
        for c in range(n):
            col_array = [grid[i][c] for i in range(n)]
            count += my_trie.search(col_array)
    
        return count    

# time O(n^2)
# space O(n^2)

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        
        # Keep track of the frequency of each row.
        row_counter = collections.Counter(tuple(row) for row in grid)

        # Add up the frequency of each column in map.
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += row_counter[tuple(col)]

            
        return count
    
# time O(n^3)
# space O(1)

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        
        # Check each row r against each column c.
        for r in range(n):
            for c in range(n):
                match = True
                
                # Iterate over row r and column c.
                for i in range(n):
                    if grid[r][i] != grid[i][c]:
                        match = False
                        break
                        
                # If row r equals column c, increment count by 1.
                count += int(match)
                    
        return count

import collections

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0

        row_graph = collections.defaultdict(list)
        col_graph = collections.defaultdict(list)

        for i in range(n):
            row_graph[tuple(grid[i])].append(i)

        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])

            col_graph[tuple(col)].append(j)

        # print(f"row graph {row_graph}, col graph {col_graph}")

        pair = set()

        for k, v in row_graph.items():
            if k in col_graph:
                for i in v:
                    for j in col_graph[k]:
                        pair.add((i, j))

        return len(pair)
