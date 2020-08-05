/**
 * @param A: an array
 * @param n: an integer
 * @return: makes the smallest absolute value of the difference between any two elements to largest
 */
 
import "sort"
import "fmt"

func maximumAbsolutValue (A []int, n int) int {
    // Write your code here
    m := len(A)
    if m == 0 {
        return 0
    }
    
    sort.Ints(A)
    
    l := 0
    r := A[len(A)-1] - A[0]
    
    fmt.Println(A, l, r)
    
    for l + 1 < r {
        mid := (l+r)/2
        if getNum(A, mid) >= n {
            l = mid
        } else {
            r = mid
        }
    }
    
    fmt.Println(l, r)
    if getNum(A, r) >= n {
        return r
    }
    if getNum(A, l) >= n {
        return l
    }
    
    return l-1
}

func getNum(a []int, gap int) int {
    cnt := 1
    last := a[0]
    
    for i := 1; i < len(a); i++ {
        if a[i] - last >= gap {
            last = a[i]
            cnt += 1
        }
    }
    
    return cnt
}
