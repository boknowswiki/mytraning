
func subsets(nums []int) [][]int {
    ret := make([][]int, 0)
    fmt.Println(ret)
    //ret = append(ret, []int{})
    //if len(nums) == 0 {
    //    return ret
    //}
    
    
    path := make([]int, 0)
    //fmt.Println(path)
    
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

