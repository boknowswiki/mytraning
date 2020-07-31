/**
 * @param dividend: the dividend
 * @param divisor: the divisor
 * @return: the result
 */
//import "fmt"

func divide (dividend int, divisor int) int {
    // write your code here
    if dividend == 0 {
        return 0
    }
    sign := 1
    if dividend < 0 {
        dividend = -dividend
        sign *= -1
    }
    if divisor == 0 {
        return 2147483647
    }
    if divisor < 0 {
        sign *= -1
        divisor = -divisor
    }
    
    var ret int
    var shift uint
    shift = 31
    
    for shift >= 0  && shift < 32{
        if dividend >= divisor << shift {
            dividend -= divisor << shift
            ret += 1 << shift
        }
        shift -= 1
        //fmt.Println(shift)
    }
    
    
    ret *= sign
    if ret > 2147483647 {
        return 2147483647
    }
    
    return ret
}


