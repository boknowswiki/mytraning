/**
 * @param x: An integer
 * @return: The sqrt of x
 */
 
//import "fmt"

func sqrt (x int) int {
    // write your code here
    if x <= 1 {
        return x
    }
    l := 1
    r := x-1
    
    for l + 1 < r {
        mid := (l+r)/2
        val := mid * mid
        //fmt.Println(mid, val)
        
        if val == x {
            return mid
        } else if val > x {
            r = mid
        } else {
            l = mid
        }
    }
    
    //fmt.Println(l, r)
    if r * r < x {
        return r
    }
    return l
}

