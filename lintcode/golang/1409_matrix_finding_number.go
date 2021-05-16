/**
 * @param mat: The matrix
 * @return: The answer
 */
func findingNumber (mat [][]int) int {
    // Write your code here
    m := len(mat)
    if m == 0 {
        return -1
    }

    n := len(mat[0])

    d := make(map[int]bool)

    for i := 0; i < m; i++ {
        level := make(map[int]bool)
        for j := 0; j < n; j++ {
            if i == 0 {
                d[mat[i][j]] = true
            }

            if d[mat[i][j]] == true {
                level[mat[i][j]] = true
            }
        }
        d = level
    }

    if len(d) != 0 {
        ret := 0
        for k, _ := range d {
            if k < ret || ret == 0 {
                ret = k
            }
        }
        return ret
    }

    return -1
}

