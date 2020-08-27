//should be good but not AC.

/**
 * @param N: That means you should return the N-th magical number.
 * @param A: Parameter A.
 * @param B: Parameter B.
 * @return: Return the N-th magical number. 
 */

//import "fmt"

func nthMagicalNumber (N int, A int, B int) int {
    // Write your code here.
    Mod := 10000000007
    
    minMulti := getMinMulti(A, B)
    
    num := minMulti/A + minMulti/B - 1
    //fmt.Println(minMulti, num)
    
    div := N/num
    divid := N%num
    
    if divid == 0 {
        return div*minMulti%Mod
    }
    
    head := []int {A, B}
    
    for i := 0; i < divid-1; i ++ {
        if head[0] <= head[1] {
            head[0] += A
        } else {
            head[1] += B
        }
    }
    
    ret := min(head[0], head[1])
    
    return (div*minMulti%Mod+ret)%Mod
}

func getMinMulti(a, b int) int {
    var gcd func (x, y int) int
    //fmt.Println(a,b)
    gcd = func (x, y int) int {
        if x == 0 {
            return y
        }
        return gcd(y%x, x)
    }
    val := a/gcd(a, b)*b
    //fmt.Println(val)
    return val
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
