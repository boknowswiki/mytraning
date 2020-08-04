/**
 * @param n: an integer
 * @param k: an integer
 * @return: how many problem can you accept
 */
 
import "fmt"
import "math"

func canAccept (n int64, k int) int64 {
    // Write your code here
    var l, r int64
    l = 0
    r = int64(math.Sqrt(float64(2*n)))
    
    for l + 1 < r {
        mid := l + (r-l)/2
        
        total := (1+mid)*mid/2*int64(k)
        
        fmt.Println(l, r, mid, total)
        if total == n {
            return mid
        } else if total < n {
            l = mid
        } else {
            r = mid
        }
    }
    
    if (1+r)*r/2*int64(k) <= n {
        return r
    }
    
    return l
}

