/**
 * @param matrix: matrix, a list of lists of integers
 * @param target: An integer
 * @return: a boolean, indicate whether matrix contains target
 */
func searchMatrix (matrix [][]int, target int) bool {
    // write your code here
    m := len(matrix)
    if m == 0 {
        return false
    }
    n := len(matrix[0])
    if n == 0 {
        return false
    }
    
    if target < matrix[0][0] || target > matrix[m-1][n-1] {
        return false
    }
    
    left := 0
    right := m*n-1
    
    for left + 1 < right {
       mid := (left+right)/2
       row := mid/n
       col := mid%n
       
       if matrix[row][col] == target {
           return true
       } else if matrix[row][col] < target {
           left = mid
       } else {
           right = mid
       }
    }
    
    if matrix[left/n][left%n] == target {
        return true
    }
    if matrix[right/n][right%n] == target {
        return true
    }

    return false    
}

