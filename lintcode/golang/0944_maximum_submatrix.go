/**
 * @param matrix: the given matrix
 * @return: the largest possible sum
 */
func maxSubmatrix (matrix [][]int) int {
    // write your code here
    ret := 0
    
    for i := 0; i < len(matrix); i++ {
        sum := make([]int, len(matrix[0]))
        for j := i; j < len(matrix); j++ {
            for k := 0; k < len(matrix[0]); k++ {
                sum[k] += matrix[j][k]
            }
            val := func (sum []int) int {
                total := 0
                ret := 0
                
                for x := 0; x < len(sum); x++ {
                    total += sum[x]
                    ret = max(ret, total)
                    total = max(total, 0)
                }
                
                return ret
            }(sum)
            ret = max(ret, val)
        }
    }
    
    return ret
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
