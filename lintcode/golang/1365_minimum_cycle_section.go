/**
 * @param array: an integer array
 * @return: the length of the minimum cycle section
 */
func minimumCycleSection (array []int) int {
    // Write your code here
    n := len(array)
    if n <= 1 {
        return n
    }
    s := make([]int, n+1)
    s[0] = -1
    l := -1
    r := 0

    for r < n {
        if l == -1 || array[r] == array[(l+n)%n] {
            l++
            r++
            s[r] = l
        } else {
            l = s[l]
        }
    }
    
    return r - s[r]
}

