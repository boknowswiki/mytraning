/**
 * @param n: Given the range of numbers
 * @param k: Given the numbers of combinations
 * @return: All the combinations of k numbers out of 1..n
 */
func combine (n int, k int) [][]int {
    // write your code here
    if n == 0 {
        return [][]int{}
    }
    
    ret := [][]int{}
    
    var dfs func(int, int, int, []int, *[][]int)
    dfs = func (n int, k int, index int, path []int, ret *[][]int) {
        if k == len(path) {
            tmp := make([]int, len(path))
            copy(tmp, path)
            *ret = append(*ret, tmp)
            return
        }
        
        for i := index; i <= n; i++ {
            path = append(path, i)
            dfs(n, k, i+1, path, ret)
            path = path[:len(path)-1]
        }
    }
    
    dfs(n, k, 1, []int{}, &ret)
    
    return ret
}

