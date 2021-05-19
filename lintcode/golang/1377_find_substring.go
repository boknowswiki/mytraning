/**
 * @param str: The string
 * @param k: The length of the substring
 * @return: The answer
 */
func findSubstring (str string, k int) int {
    // Write your code here
    n := len(str)
    if n == 0  || n < k{
        return 0
    }

    gMap := make(map[string]bool)
    lMap := make(map[string]int)
    l, r := 0, 0
    subStr := ""
    ret := 0
    for r < n {
        subStr = subStr + string(str[r])
        lMap[string(str[r])] += 1
        for len(lMap) > k || lMap[string(str[r])] > 1 {
            lMap[string(str[l])]--
            if lMap[string(str[l])] == 0 {
                delete(lMap, string(str[l]))
            }
            l++
            subStr = subStr[1:]
        }
        if len(lMap) == k && gMap[subStr] == false {
            gMap[subStr] = true
            ret++
        }
        r++
    }

    return ret
}

