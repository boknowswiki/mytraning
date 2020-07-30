/**
 * @param A: An integer array
 * @param start: An integer
 * @param end: An integer
 * @return: the number of possible answer
 */
 
//import "fmt"

func subarraySumII (A []int, start int, end int) int {
    // write your code here
    n := len(A)
    if n == 0 {
        return 0
    }
    
    pre_sum := make([]int, len(A)+1)
    
    for i, val := range A {
        pre_sum[i+1] += pre_sum[i] + val
    }
    
    //fmt.Println(pre_sum, len(pre_sum))
    
    l := 0
    r := 0
    var ret int
    
    for i, _ := range pre_sum {
        for l < i && pre_sum[i] - pre_sum[l] > end {
            l += 1
        }
        for r < i && pre_sum[i] - pre_sum[r] >= start {
            r += 1
        }
        
        ret += r-l
        //fmt.Println(i, l, r, ret)
    }
    
    return ret
}

