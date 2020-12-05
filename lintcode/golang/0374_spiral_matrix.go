/**
 * @param matrix: a matrix of m x n elements
 * @return: an integer list
 */
func spiralOrder (matrix [][]int) []int {
    // write your code here
    ret := []int{}
    if matrix == nil || len(matrix) == 0 {
        return ret
    }
    
    m, n := len(matrix), len(matrix[0])
    
    x, y := 0, 0
    
    for m > 0 && n > 0 {
        if m == 1 {
            for i := 0; i < n; i++ {
                ret = append(ret, matrix[x][y])
                y++
            }
            break
        } else if n == 1 {
            for i := 0; i < m; i++ {
                ret = append(ret, matrix[x][y])
                x++
            }
            break
        }
        
        for i := 0; i < n-1; i++ {
            ret = append(ret, matrix[x][y])
            y++
        }
        
        for i := 0; i < m-1; i++ {
            ret = append(ret, matrix[x][y])
            x++
        }
        
        for i := n-1; i > 0; i-- {
            ret = append(ret, matrix[x][y])
            y--
        }
        
        for i := m-1; i> 0; i-- {
            ret = append(ret, matrix[x][y])
            x--
        }
        
        x++
        y++
        m = m-2
        n = n-2
    }
    
    return ret
}

