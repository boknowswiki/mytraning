/**
 * @param n: An integer
 * @return: a square matrix
 */
func generateMatrix (n int) [][]int {
    // write your code here
    if n == 0 {
        return [][]int{}
    }
    
    ret := make([][]int, n)
    for i := 0; i < n; i++ {
        ret[i] = make([]int, n)
    }
    
    x := 0
    y := 0
    num := 1
    
    for n > 0 {
        if n == 1 {
            ret[x][y] = num
            num++
            break
        }
        
        for i := 0; i < n-1; i++ {
            ret[x][y] = num
            y++
            num++
        }
        
        for i := 0; i < n-1; i++ {
            ret[x][y] = num
            x++
            num++
        }
        
        for i := n-1; i > 0; i-- {
            ret[x][y] = num
            y--
            num++
        }
        
        for i:= n-1; i > 0; i-- {
            ret[x][y] = num
            x--
            num++
        }
        
        x++
        y++
        n -= 2
    }
    
    return ret
}

