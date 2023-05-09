#!/usr/bin/python -t


# matrix, array
# time O(m*n)
# space O(1)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left = up = 0
        right = n-1
        down = m-1
        ret = []

        while len(ret) < m*n:
            # left to right
            for i in range(left, right+1):
                ret.append(matrix[up][i])

            # up to down
            for i in range(up+1, down+1):
                ret.append(matrix[i][right])
            
            # make sure on a different row
            if up != down:
                for i in range(right-1, left-1, -1):
                    ret.append(matrix[down][i])

            # make sure on different col
            if left != right:
                for i in range(down-1, up, -1):
                    ret.append(matrix[i][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return ret
    

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101
        rows, columns = len(matrix), len(matrix[0])
        # Four directions that we will move: right, down, left, up.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction: moving right.
        current_direction = 0
        # The number of times we change the direction.
        change_direction = 0
        # Current place that we are at is (row, col).
        # row is the row index; col is the column index.
        row = col = 0
        # Store the first element and mark it as visited.
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction < 2:

            while True:
                # Calculate the next place that we will move to.
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # Break if the next step is out of bounds.
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                # Break if the next step is on a visited cell.
                if matrix[next_row][next_col] == VISITED:
                    break

                # Reset this to 0 since we did not break and change the direction.
                change_direction = 0
                # Update our current position to the next step.
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # Change our direction.
            current_direction = (current_direction + 1) % 4
            # Increment change_direction because we changed our direction.
            change_direction += 1

        return result
    
    
    
    
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        ret = []
        if m == 0:
            return ret
        n = len(matrix[0])
        row = 0
        col = -1

        while True:
            #left to right
            for i in xrange(n):
                col = col + 1
                ret.append(matrix[row][col])

            m = m - 1
            if m == 0:
                break

            #top to bottom
            for i in xrange(m):
                row = row + 1
                ret.append(matrix[row][col])

            n = n - 1
            if n == 0:
                break

            #right to left
            for i in xrange(n):
                col = col - 1
                ret.append(matrix[row][col])

            m = m - 1
            if m == 0:
                break
            #bottom to top
            for i in xrange(m):
                row = row - 1
                ret.append(matrix[row][col])

            n = n - 1
            if n == 0:
                break

        return ret

