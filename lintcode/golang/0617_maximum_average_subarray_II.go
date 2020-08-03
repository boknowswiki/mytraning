
// should be correct, but not AC
/**
 * @param nums: an array with positive and negative numbers
 * @param k: an integer
 * @return: the maximum average
 */
 
import "fmt"

func maxAverage (nums []int, k int) float64 {
    // write your code here
    n := len(nums)
    if n == 0 {
        return 0
    }
    
    l := min(nums)
    r := max(nums)
    
    for l + 0.0001 < r {
        mid := (l+r)/2
        
        if canFind(nums, k, mid) {
            l = mid
        } else {
            r = mid
        }
    }
    
    return l
}

func max(nums []int) float64 {
    var ret int
    ret = nums[0]
    
    for _, n := range nums {
        if n > ret {
            ret = n
        }
    }
    return float64(ret)
}

func min(nums []int) float64 {
    var ret int
    ret = nums[0]
    
    for _, n := range nums {
        if n < ret {
            ret = n
        }
    }
    return float64(ret)
}

func canFind(nums []int, k int, target float64) bool {
    pre_sum := []float64{0}
    
    for _, v := range nums {
        pre_sum = append(pre_sum, pre_sum[len(pre_sum)-1] + float64(v)- target)
    }
    
    var min_pre float64
    
    for i:= k; i < len(nums)+ 1; i++ {
        if pre_sum[i] - min_pre >= 0 {
            return true
        }
        fmt.Println(i, k, pre_sum)
        min_pre = min_float64(min_pre, pre_sum[i-k+1])
    }
    
    return false
}

func min_float64(a, b float64) float64 {
    if a < b {
        return a
    }
    return b
}
