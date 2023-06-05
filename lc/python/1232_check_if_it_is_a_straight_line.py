# math

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n < 3:
            return True

        def diff_x(a, b):
            return a[0] - b[0]
        
        def diff_y(a, b):
            return a[1] - b[1]

        delta_x = diff_x(coordinates[1], coordinates[0])
        delta_y = diff_y(coordinates[1], coordinates[0])

        for i in range(2, n):
            if delta_x * diff_y(coordinates[i], coordinates[0]) != delta_y * diff_x(coordinates[i], coordinates[0]):
                return False

        return True
