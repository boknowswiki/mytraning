/**
 * @param n: An integer
 * @param times: an array of integers
 * @return: an integer
 */
func copyBooksII (n int, times []int) int {
    // write your code here
    l := 0
    r := times[0] * n
    
    for l + 1 < r {
        mid := l + (r-l)/2
        if canCopy(n, times, mid) {
            r = mid
        } else {
            l = mid
        }
    }
    
    if canCopy(n, times, l) {
        return l
    }
    return r
}

func canCopy(n int, times []int, target int) bool {
    var books int
    
    for _, v := range times {
        books += target/v
    }
    if books >= n {
        return true
    }
    return false
}
