/**
 * @param num: Given the candidate numbers
 * @param target: Given the target number
 * @return: All the combinations that sum to target
 */
 
import "sort"

func combinationSum2 (num []int, target int) [][]int {
    // write your code here
    if len(num) == 0 {
        return [][]int{}
    }
    
    sort.Ints(num)
    ret := [][]int{}
    
    var dfs func ([]int, int, int, []int, *[][]int)
    
    dfs = func (num []int, target int, index int, path []int, ret *[][]int) {
        if target == 0 {
            tmp := make([]int, len(path))
            copy(tmp, path)
            *ret = append(*ret, tmp)
            return
        }
        
        for i := index; i < len(num); i++ {
            if i != index && num[i] == num[i-1] {
                continue
            }
            if target - num[i] < 0 {
                break
            }
            path = append(path, num[i])
            dfs(num, target-num[i], i+1, path, ret)
            path = path[:len(path)-1]
        }
        
        return
    }
    
    dfs(num, target, 0, []int{}, &ret)
    
    return ret
}

