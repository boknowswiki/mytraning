/**
 * @param s: The capacity of backpack
 * @param v: The value of goods 
 * @param c: The capacity of goods
 * @return: The answer
 */
func getMaxValue (s int, v []int, c []int) int64 {
    // Write your code here
    index := make([]int, len(v))
    for i := len(v)-1; i >= 0; i-- {
        index[len(v)-1-i] = i
    }
    
    pre_sum := make([]int, len(v))
    pre_sum[len(v)-1] = v[len(v)-1]
    
    for i := len(v)-2; i >= 0; i-- {
        pre_sum[i] = pre_sum[i+1] + v[index[i]]
    }
    
    var ret int64
    var helper func(int, int, int)
    helper = func (start int, val int, vol int) {
        if vol > s {
            return
        }
        if int64(val) > ret {
            ret = int64(val)
        }
        if start >= len(v) || int64(val + pre_sum[start]) <= ret {
            return
        }
        helper(start+1, val+v[index[start]], vol+c[index[start]])
        helper(start+1, val, vol)
    }
    
    helper(0, 0, 0)
    
    return ret
}

