/**
 * @param nums: An integer array
 * @return: The length of LIS (longest increasing subsequence)
 */
 
//import "fmt"

func longestIncreasingSubsequence (nums []int) int {
    // write your code here
    n := len(nums)
    if n == 0 || (n == 1 && nums[0] == 0){
        return 0
    }
    
    //fmt.Println(nums, n, cap(nums))
    
    ret := make([]int, 0)
    ret = append(ret, nums[0])

    for _, val := range nums[1:] {
        if val > ret[len(ret)-1] {
            ret = append(ret, val)
        } else {
            index := findLower(ret, val)
            //fmt.Println(ret, val, index)
            ret[index] = val
        }
    }
    
    return len(ret)
}

func findLower(nums []int, val int) int {
    l := 0
    r := len(nums)
    
    for l + 1 < r {
        mid := (l+r)/2
        if nums[mid] >= val {
            r = mid
        } else {
            l = mid
        }
    }
    
    if val > nums[l] {
        return r
    }
    
    return l
}

