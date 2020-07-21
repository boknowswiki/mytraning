/**
 * @param A: an integer sorted array
 * @param target: an integer to be inserted
 * @return: An integer
 */
 
//import "fmt"
func searchInsert (A []int, target int) int {
    // write your code here
    n := len(A)
    //fmt.Println(n)
    if n == 0 {
        return 0
    }
    
    left := 0
    right := n-1
    
    for left + 1 < right {
        mid := (left+right)/2
        
        if A[mid] == target {
            return mid
        } else if A[mid] > target {
            right = mid
        } else {
            left = mid
        }
    }
    
    //fmt.Println(left, right)
    //fmt.Println(A[left], A[right])
    
    if A[left] >= target {
        return left
    }
    
    if right != 0 && A[right] < target {
        return right+1
    }
    
    return right
}

