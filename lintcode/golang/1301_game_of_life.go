/**
 * @param board: the given board
 * @return: nothing
 */
func gameOfLife (board *[][]int)  {
    // Write your code here
    if len(*board) == 0 || len((*board)[0]) == 0 {
        return
    }
    
    m := len(*board)
    n := len((*board)[0])
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            var liveNeighbors func([][]int, int, int) int
            
            liveNeighbors = func (s [][]int, x int, y int) int {
                ret := 0
                for a := max(x-1, 0); a <= min(x+1, m-1); a++ {
                    for b := max(y-1, 0); b <= min(y+1, n-1); b++ {
                        ret += s[a][b]&1
                    }
                }
                
                ret -= s[x][y]&1
                return ret
            }
            
            neighs := liveNeighbors(*board, i, j)
            if (*board)[i][j] == 1 && neighs >= 2 && neighs <= 3 {
                (*board)[i][j] = 3
            }
            if (*board)[i][j] == 0 && neighs == 3 {
                (*board)[i][j] = 2
            }
        }
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            (*board)[i][j] >>= 1
        }
    }
    
    return
}
