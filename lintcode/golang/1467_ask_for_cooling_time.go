/**
 * @param arr: The release order
 * @param n: The cooldown
 * @return: Return the time
 */
func askForCoolingTime (arr []int, n int) int {
    // Write your code here
    l := len(arr)
    if l == 0 {
        return 0
    }

    d := make(map[int]int)
    ret := 0

    for _, v := range arr {
        ret++
        if pre, ok := d[v]; ok {
            if ret - pre <= n {
                ret = pre+n+1
            }
        }
        d[v] = ret
    }

    return ret
}

