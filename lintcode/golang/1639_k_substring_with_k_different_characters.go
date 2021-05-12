/**
 * @param stringIn: The original string.
 * @param K: The length of substrings.
 * @return: return the count of substring of length K and exactly K distinct characters.
 */
func KSubstring (stringIn string, K int) int {
    // Write your code here
    subMap := make(map[string]int)
    foundSub := make(map[string]int)
    r := 0
    for l := 0; l <= len(stringIn)-K; l++ {
        for r < len(stringIn) && len(subMap) < K {
            if _, ok := subMap[string(stringIn[r])]; !ok {
                subMap[string(stringIn[r])] = 1
                r++
                if len(subMap) == K {
                    foundSub[string(stringIn[l:r])] = 1
                }
            } else {
                break
            }
        }
        delete(subMap, string(stringIn[l]))
    }

    return len(foundSub)
}

