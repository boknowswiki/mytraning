# hash table, matrix
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
