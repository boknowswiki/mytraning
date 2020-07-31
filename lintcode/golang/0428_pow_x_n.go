/**
 * @param x: the base number
 * @param n: the power number
 * @return: the result
 */
func myPow (x float64, n int) float64 {
    // write your code here
    if n == 0 {
        return 1
    }
    
    if n < 0 {
        x = 1/x
        n = -n
    }
    
    var ret float64
    ret = 1
    tmp := x
    
    for n > 0 {
        if n % 2 == 1 {
            ret *= tmp
        }
        
        tmp *= tmp
        n = n/2
    }
    
    return ret
}

