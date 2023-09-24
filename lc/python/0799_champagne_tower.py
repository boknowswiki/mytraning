# dp
# time O(row^2)
# space O(row^2)

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0]*(i+1) for i in range(query_row+1)]
        tower[0][0] = poured

        for r in range(query_row):
            for c in range(len(tower[r])):
                champagne = (tower[r][c]-1) / 2
                if champagne > 0:
                    tower[r+1][c] += champagne
                    tower[r+1][c+1] += champagne

        return min(1, tower[query_row][query_glass])
        
