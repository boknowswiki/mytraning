
import "fmt"

/**
 * @param nums: A set of numbers
 * @return: A list of lists
 */
func subsets (nums []int) [][]int {
    // write your code here
    ret := make([][]int, 0)
    fmt.Println(ret)
    if len(nums) == 0 {
        return ret
    }
    
    
    path := make([]int, 0)
    
    helper(nums, 0, path, &ret)
    
    
    
    return ret
}

func helper(nums []int, index int, path []int, ret *[][]int) {
    tmp := make([]int, len(path))
    copy(tmp, path)
    *ret = append(*ret, tmp)
    
    for i := index; i < len(nums); i++ {
        path = append(path, nums[i])
        helper(nums, i+1, path, ret)
        path = path[:len(path)-1]
    }
}
