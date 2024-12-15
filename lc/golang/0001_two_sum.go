//time O(n)
//space O(n)

func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    for i := 0; i < len(nums); i++ {
        need := target - nums[i]
        v, ok := m[need]
        if ok {
            return []int{v, i}
        }
        m[nums[i]] = i
    }

    return []int{-1, -1}
}
