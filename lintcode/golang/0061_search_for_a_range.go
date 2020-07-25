/**
 * @param A: an integer sorted array
 * @param target: an integer to be inserted
 * @return: a list of length 2, [index1, index2]
 */
 
//import "fmt"

func searchRange (A []int, target int) []int {
    // write your code here
    n := len(A)
    ret := []int {-1, -1}
    if n == 0 {
        return ret
    }
    
    ret[0] = lower(A, target)
    ret[1] = upper(A, target)
    
    return ret
}

func lower(a []int, target int) int {
    l := 0
    r := len(a)-1
    
    for l+1 < r {
        mid := (l+r)/2
        if a[mid] >= target {
            r = mid
        } else {
            l = mid
        }
    }
    
    if a[l] == target {
        return l
    }
    if a[r] == target {
        return r
    }
    
    //fmt.Println(l, r)
    return -1
}

func upper(a []int, target int) int {
    l := 0
    r := len(a)-1
    
    for l+1 < r {
        mid := (l+r)/2
        if a[mid] <= target {
            l = mid
        } else {
            r = mid
        }
    }
    
    if a[r] == target {
        return r
    }
    if a[l] == target {
        return l
    }

    return -1
}
