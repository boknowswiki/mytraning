/**
 * @param A: A an integer array sorted in ascending order
 * @param target: An integer
 * @return: An integer
 */
 
//import "fmt"

func totalOccurrence (A []int, target int) int {
    // write your code here
    n := len(A)
    if n == 0 {
        return 0
    }
    
    //fmt.Println(n)
    lower := findLower(A, target)
    upper := findUpper(A, target)
    
    //fmt.Println(lower, upper)
    if upper == -1 && lower == -1 {
        return 0
    }
    return upper - lower + 1
}

func findLower(A []int, target int) int {
    n := len(A)
    l := 0
    r := n-1
    
    for l+1 < r {
        mid := (l+r)/2
        
        if A[mid] >= target {
            r = mid
        } else {
            l = mid
        }
    }
    
    if A[l] == target {
        return l
    }
    if A[r] == target {
        return r
    }
    
    return -1
}

func findUpper(A []int, target int) int {
    n := len(A)
    l := 0
    r := n-1
    
    for l+1 < r {
        mid := (l+r)/2
        
        if A[mid] <= target {
            l = mid
        } else {
            r = mid
        }
    }
    
    if A[r] == target {
        return r
    }
    if A[l] == target {
        return l
    }
    
    return -1
}
