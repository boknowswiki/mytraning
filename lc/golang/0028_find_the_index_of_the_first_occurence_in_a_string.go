// time O(mn)
// space O(1)

func strStr(haystack string, needle string) int {
    for i := 0; ; i++ {
        for j := 0; ; j++ {
            if j == len(needle) {
                return i
            }
            if i+j == len(haystack) {
                return -1
            }
            if haystack[i+j] != needle[j] {
                break
            }
        }
    }
    return -1
}
