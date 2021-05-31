//hash

/**
 * @param arrs: the arrays
 * @return: the number of the intersection of the arrays
 */
import "fmt"
func intersectionOfArrays (arrs [][]int) int {
    // write your code here
    n := len(arrs)
    fmt.Println(n)
    exists := make(map[int]int)
    for i := 0; i < n; i++ {
        fmt.Println("len: ", len(arrs[i]))
        if len(arrs[i]) == 1 && arrs[i][0] == 0 {
            continue
        }
        for _, v := range arrs[i] {
            fmt.Println(v)
            exists[v]++
        }
    }

    fmt.Println(exists)

    ret := 0
    for _, v := range exists {
        if v == n {
            ret++
        }
    }

    return ret
}

