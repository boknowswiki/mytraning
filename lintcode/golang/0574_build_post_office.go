/**
 * @param grid: a 2D grid
 * @return: An integer
 */
func shortestDistance (grid [][]int) int {
    // write your code here
    m := len(grid)
    if m == 0 {
        return 0
    }
    n := len(grid[0])
    if n == 0 {
        return 0
    }
    
    rowCnt := make([]int, m)
    colCnt := make([]int, n)
    rowDist := make([]int, m)
    colDist := make([]int, n)
    var ret int
    ret = 1 << 31 -1
    
    for i, r := range grid {
        for j, _ := range r {
            if grid[i][j] == 1 {
                rowCnt[i] += 1
                colCnt[j] += 1
            }
        }
    }
    
    for i, _ := range grid {
        for j, _ := range grid {
            rowDist[i] += rowCnt[j] * abs(j - i)
        }
    }
    
    for i, _ := range grid[0] {
        for j, _ := range grid[0] {
            colDist[i] += colCnt[j] * abs(j - i)
        }
    }
    
    for i, r := range grid {
        for j, _ := range r {
            if grid[i][j] == 0 {
                tmp := rowDist[i] + colDist[j]
                if tmp < ret {
                    ret = tmp
                }
            }
        }
    }
    
    return ret
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
