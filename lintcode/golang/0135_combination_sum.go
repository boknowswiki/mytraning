/**
 * @param candidates: A list of integers
 * @param target: An integer
 * @return: A list of lists of integers
 */
 
import "sort"

func combinationSum (candidates []int, target int) [][]int {
    // write your code here
    sort.Ints(candidates)
    
    n := len(candidates)
    if n == 0 {
        return [][]int{}
    }
    
    ret := [][]int{}
    
    dfs(candidates, target, 0, &[]int{}, &ret)
    
    return ret
}

func dfs(candidates []int, target int, index int, path *[]int, ret *[][]int) {
    if target < 0 {
        return
    }
    
    if target == 0 {
        tmp := make([]int, len(*path))
        copy(tmp, *path)
        *ret = append(*ret, tmp)
        
        return
    }
    
    for i := index; i < len(candidates); i++ {
        if target - candidates[i] < 0 {
            break
        }
        if i != index && candidates[i] == candidates[i-1] {
            continue
        }
        *path = append(*path, candidates[i])
        dfs(candidates, target - candidates[i], i, path, ret)
        *path = (*path)[:len(*path)-1]
    }
    
    return
}
